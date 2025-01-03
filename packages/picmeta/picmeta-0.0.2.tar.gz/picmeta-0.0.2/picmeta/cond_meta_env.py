"""
Variant of meta_env for conditional setting

So far, computations seem to exhibit much more instability than unconditional metalearning setting

TO DO:
- check time used for reassigning accu_sample_val fields for the train method
"""

from typing import Callable

import numpy as np

from picproba.types import ProbaParam
from picmeta.types import MetaData, MetaParam
from picpacbayes import pacbayes_minimize
from picmeta.hist_meta import HistMeta
from picmeta.meta_env import MetaLearningEnv
from picmeta.task import Task
from apicutils import blab
from picproba import ProbaMap


class CondMetaEnv(MetaLearningEnv):
    r"""Conditional Meta Learning environnement for Variational Catoni Pac Bayes

    For a collection of task, meta learns a suitable map from metadata to prior.

    Class attributes:
    - proba_map: A ProbaMap instance, defining the shared family of probabilities in which the meta
    prior is learnt, and in which the tasks' posterior live.
    - list_tasks: A list of Task objects. All tasks should share the same parameter space, coherent
    with the proba_map attribute (this is not checked, training will fail).
    - meta_param: MetaParam, containing the current meta parameter.
    - cond_map, the map from task meta data and meta parameter to a ProbaParam
    - der_cond_map, the derivative of cond_map with respect to the meta parameter
    - hyperparams: dictionary, containing hyperparameters for training each task.
    - hist_meta: HistMeta, track the evolution of score and prior_param during training
    - n_task: int, the number of tasks
    - task_score: the list of end penalised score for each task
    - converged: boolean, specifying if convergence has been reached
    - meta_score: float, the current meta score for the prior


    Routine motivation:
    In the context of penalised risk minimisation inner algorithm, the meta gradient is easy to
    compute (see below). As such, the meta training algorithm is a Gradient descent procedure. To
    improve stability, the prior distribution is forced to evolve slowly (in term of KL divergence)

    Gradient of the meta score for Catoni Pac-Bayes.
    For a proba map $\pi$, noting $\theta_0$ the prior parameter, $R_i$, $\lambda_i$ the score
    function and temperature for task $i$, $\hat{\theta}_i = \hat{\theta}_i(\theta_0)$ the
    posterior parameter using prior $\theta_0$, the meta score of prior parameter $\theta_0$ is
    defined as $ S(\theta_0) = \sum_i S_i(\theta_0) $ where
        $$ S_i(\theta_0)
        = \pi(\hat{\theta}_i)[R_i] + \lambda_i KL(\pi(\hat{\theta}_i), \pi(\theta_0))$$

    In the context of conditional meta learning, the prior is constructed from a meta parameter,
    which is learnt, and taks meta data $m_i$. As such, the meta score of meta param $\alpha$ is
    defined as:

        $$ S(\alpha) = \sum_i S_i(T(\alpha, m_i)) $$

    where $T$ is the map from meta data to prior parameter. Noting $\theta_i = T(\alpha, m_i)$,
    the derivative of $S_i(\theta_i)$ with respect to $\theta_i$ has simple expression
    $\lambda_i K_i$ where $K_i$ is the gradient of the Kullback--Leibler term
    $KL(\pi(\hat{\theta}_i), \pi(\theta_i))$ with respect to $\theta_i$ at fixed $\hat{\theta}_i$
    value. Therefore, the gradient of $S_i(T(\alpha, m_i))$ with respect to $\alpha$ can be
    computed using the chain rule.
    """

    def __init__(
        self,
        proba_map: ProbaMap,
        list_task: list[Task],
        cond_map: Callable[[MetaParam, MetaData], ProbaParam],
        der_cond_map: Callable[[MetaParam, MetaData], np.ndarray],
        meta_param: MetaParam,
        **hyperparams,
    ):
        """Initialize conditional meta learning environnement.

        Args:
            proba_map (ProbaMap): class of distributions on which priors/posterior are optimized
            list_task (list[Task]): list of learning task constituing the meta learning
                environnement
            cond_map (Callable): map task meta data and meta parameter to a ProbaParam
            der_cond_map (Callable): derivative of cond_map with respect to the meta parameter
            meta_param (MetaParam): initial Meta parameter value.
            **hyperparams (dict): further arguments passed to pacbayes_minimize (inner
                learning algorithm).
        """
        super().__init__(proba_map=proba_map, list_task=list_task, **hyperparams)

        self.meta_param = np.array(meta_param)

        self.cond_map = cond_map
        self.der_cond_map = der_cond_map

        self._meta_shape = self.meta_param.shape
        self.hist_meta = HistMeta(
            meta_param_shape=self._meta_shape, n=1, n_task=self.n_task
        )
        self.hist_meta.add1(self.meta_param, np.nan, self.task_score)  # type: ignore

        self._prob_ndim = len(proba_map.proba_param_shape)

    def train(self, task: Task) -> None:
        """Perform inner learning for a task using learning environnement prior.

        Posterior and the accu sample val are update in place in the task.

        The inner algorithm called is 'aduq.bayes.pacbayes_minimize.' The routine used depends
        on the proba_map and hyperparams attributes of the learning environnement (pre inferred
        at construction time).

        The 'accu_sample_val' field of the task is indirectly augmented by pacbayes_minimize.
        """
        # Infer the prior_param from the conditional mapping with meta_param
        prior_param = self.cond_map(self.meta_param, task.meta_data)

        # Perform the inner algorithm
        opt_res = pacbayes_minimize(
            fun=task.score,
            proba_map=self.proba_map,
            prior_param=prior_param,
            post_param=task.post_param,
            temperature=task.temp,
            prev_eval=task.accu_sample_val,
            vectorized=task.vectorized,
            parallel=task.parallel,
            **self.hyperparams,
        )

        # Store output in task
        task.post_param = opt_res.opti_param
        task.end_score = opt_res.opti_score  # type: ignore

    def grad_meta(self, task: Task, n_grad_KL: int = 10**4) -> ProbaParam:
        """Compute the meta gradient for a provided task.

        Arg:
            task: a Task object.

        Output:
            The gradient of the penalised meta score with respect to the meta parameter.
        """
        # Perform the inner algorithm
        self.train(task)

        # Recompute the prior parameter
        prior_param = self.cond_map(self.meta_param, task.meta_data)  # type: ignore

        # Compute the gradient of the meta parameter as temp * J meta_to_prior @ nabla_2 KL

        return task.temp * np.tensordot(
            self.der_cond_map(self.meta_param, task.meta_data),
            self.proba_map.grad_right_kl(task.post_param)(prior_param, n_grad_KL)[0],  # type: ignore
            (
                tuple(range(-self._prob_ndim, 0)),
                tuple(range(self._prob_ndim)),
            ),
        )

    def meta_learn(
        self, epochs: int = 1, eta: float = 0.01, silent: bool = False
    ) -> None:
        """Meta Learning algorithm

        Args:
            epochs (int): number of learning epochs (default 1)
            eta (float): step size for gradient descent (default 0.01)
            silent (bool): should there be any print

        Outputs:
            None (modifications inplace)

        The tasks are read one after another and the meta_param is updated after each task is read.
        Difference with MetaLearnEnv: the meta_param rather than prior_param is updated
        """
        # Extend history for meta learning log
        self.hist_meta.extend_memory(epochs)

        # Extend memory for tasks (once and for all rather than iteratively)
        def _extend_memo(task: Task):
            n_remain = task.accu_sample_val.n_remain()  # type: ignore
            n_fill = epochs * self.hyperparams["per_step"]
            if n_fill < n_remain:
                task.accu_sample_val.extend_memory(n_fill - n_remain)  # type: ignore

        [_extend_memo(task) for task in self.list_task]  # pylint: disable=W0106

        # Define step size
        eta_loc = eta / self.n_task

        # Main learning loop
        for i in range(epochs):
            blab(silent, f"Iteration {i}/{epochs}")

            # Iterate over tasks
            for j, task in enumerate(self.list_task):
                blab(silent, f"Starting task {j}/{self.n_task}")
                # Compute gradient (this updates task posterior automatically)
                grad = self.grad_meta(task)
                # Store end score for task
                self.task_score[j] = task.end_score
                # Update meta param
                self.meta_param = self.meta_param - eta_loc * grad

            # Log meta learning result
            self.meta_score = np.mean(self.task_score)
            self.hist_meta.add1(self.meta_param, self.meta_score, self.task_score)  # type: ignore

            blab(silent, f"Meta score: {self.meta_score}\n")

    def meta_learn_batch(
        self, epochs: int = 1, eta: float = 0.01, silent: bool = False
    ):  # pylint: disable=W0221
        """
        Meta Learning algorithm (batch variant)

        Args:
            epochs (int): number of learning epochs (default 1)
            eta (float): step size for gradient descent (default 0.01)
            silent (bool): should there be any print

        Outputs:
            None (modifications inplace)

        The prior is updated after all tasks have been read. Improves stability at the cost of
        duration (for the early stages) compared to non batch version.
        """
        # Extend history for meta learning log
        self.hist_meta.extend_memory(epochs)

        # Extend task memory
        def _extend_memo(task: Task):
            n_remain = task.accu_sample_val.n_remain()  # type: ignore
            n_fill = epochs * self.hyperparams["per_step"]
            if n_fill < n_remain:
                task.accu_sample_val.extend_memory(n_fill - n_remain)  # type: ignore

        [_extend_memo(task) for task in self.list_task]  # pylint: disable = W0106

        # Define step size
        eta_loc = eta / self.n_task

        # Main learning loop
        for i in range(epochs):
            blab(silent, f"Iteration {i}")
            # Prepare accu for gradient
            grad = np.zeros(self._meta_shape)

            # Iterate over tasks
            for j, task in enumerate(self.list_task):
                blab(silent, f"Starting task {j}")
                # Compute gradient (this updates task posterior automatically)
                grad = grad - self.grad_meta(task)

                # Store end score for task
                self.task_score[j] = task.end_score

            # Compute new meta param
            new_meta_param = self.meta_param + eta_loc * grad

            # Log/update meta learning result
            self.meta_param = new_meta_param
            self.meta_score = np.mean(self.task_score)
            self.hist_meta.add1(self.meta_param, self.meta_score, self.task_score)

            blab(silent, f"Meta score: {self.meta_score}\n")
