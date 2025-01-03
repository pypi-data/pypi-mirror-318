"""Meta Learning Environment class for Variational Catoni PAC Bayes"""

import os
import warnings
from typing import Optional, Union

import dill
import numpy as np

from picproba.types import ProbaParam
from picoptim.fun_evals import FunEvals
from picpacbayes import (
    FunEvalsDens,
    FunEvalsExp,
    infer_pb_routine,
    pacbayes_minimize,
)
from picmeta.hist_meta import HistMeta
from picmeta.task import Task
from apicutils import blab, prod
from picoptim import dichoto, Adamizer
from picproba import PreExpFamily, ProbaMap, RenormError


KL_COND_DECODE = {
    "left":0,
    "right":1,
    "mean":2,
    "max":3,
    "min":4,
    "avg":2,
    0:0,
    1:1,
    2:2,
    3:3,
    4:4
}

KL_COND_STR = {
    0:"KL(new, old) < kl_max",
    1:"KL(old, new) < kl_max",
    2:".5 KL(old, new) + .5 KL(new, old) < kl_max",
    3: "max(KL(old, new), KL(new, old)) < kl_max",
    4: "min(KL(old, new), KL(old, new)) < kl_max"
}

class EnforceKL:
    """KL condition to enforce when computing update
    There are 5 types of KL condition which can be enforced
    0: KL(new, old) < kl_max
    1: KL(old, new) < kl_max
    2: .5 (KL(old, new) + KL(new, old)) < kl_max
    3: max(KL(old, new), KL(new, old)) < kl_max
    4: min(KL(old, new), KL(old, new)) < kl_max

    where new = old + alpha * direction

    """
    def __init__(
        self,
        proba_map:ProbaMap,
        prior_param: ProbaParam,
        direction: np.ndarray,
        kl_max:float,
        alpha_max:float,
        work_in_t:bool,
        kl_type:Union[int, str]=0,
        n_sample_kl:int=1000,
        y_pres:Optional[float]=None,
        x_pres:Optional[float]=None,
        m_max:int=100):

        self.proba_map = proba_map

        self.prior_param = prior_param
        self.direction = direction

        self.kl_max = kl_max
        self.alpha_max = alpha_max

        self.work_in_t = work_in_t
        
        self.kl_type = kl_type

        self.n_sample_kl = n_sample_kl

        self.y_pres = y_pres
        self.x_pres = x_pres
        self.m_max = m_max
    
    @property
    def kl_type(self)->int:
        return self._kl_type

    @kl_type.setter
    def kl_type(self, value):
        # Add more explicit error here
        typ = KL_COND_DECODE[value]

        self._kl_type = value

        if self.work_in_t:
            def par_from_alpha(alpha):
                return self.proba_map.T_to_param(self.prior_param + alpha * self.direction)
        else:
            def par_from_alpha(alpha):
                return self.prior_param + alpha * self.direction

        if typ == 0:
            # Using KL(new, old)
            def kl_fun(alpha):
                new_prior_param = par_from_alpha(alpha)
                return self.proba_map.kl(new_prior_param, self.prior_param, self.n_sample_kl)
        elif typ == 1:
            # Using KL(old, new)
            def kl_fun(alpha):                
                new_prior_param = par_from_alpha(alpha)
                return self.proba_map.kl(self.prior_param, new_prior_param, self.n_sample_kl)
        elif typ == 2:
            # Using (KL(new, old) + KL(old, new))/2
            def kl_fun(alpha):
                new_prior_param = par_from_alpha(alpha)
                return .5 * (
                    self.proba_map.kl(self.prior_param, new_prior_param, self.n_sample_kl)
                    + self.proba_map.kl(new_prior_param, self.prior_param, self.n_sample_kl)
                    )
        elif typ == 3:
            # Using max(KL(new, old), KL(old, new))
            def kl_fun(alpha):
                new_prior_param = par_from_alpha(alpha)
                return max(
                    self.proba_map.kl(self.prior_param, new_prior_param, self.n_sample_kl),
                    self.proba_map.kl(new_prior_param, self.prior_param, self.n_sample_kl)
                    )
            
        elif typ == 4:
            # Using min((KL(new, old), KL(old, new))
            def kl_fun(alpha):
                new_prior_param = par_from_alpha(alpha)
                return min(
                    self.proba_map.kl(self.prior_param, new_prior_param, self.n_sample_kl),
                    self.proba_map.kl(new_prior_param, self.prior_param, self.n_sample_kl)
                    )
            
        else:
            raise ValueError(f"Unknown {typ} ")

        self.kl_fun = kl_fun
        
    def enforce(self)->float:
        """Find largest alpha < alpha_max such that the KL condition is satisfied.
        The KL condition depends on the kl_type:
            0: KL(new, old) < kl_max
            1: KL(old, new) < kl_max
            2: .5 (KL(old, new) + KL(new, old)) < kl_max
            3: max(KL(old, new), KL(new, old)) < kl_max
            4: min(KL(old, new), KL(old, new)) < kl_max
        """
        return dichoto(
            self.kl_fun,
            self.kl_max,
            x_min=0,
            x_max=self.alpha_max,
            increasing=True,
            y_pres=self.y_pres,
            x_pres=self.x_pres,
            m_max=self.m_max,
        )[0]

def _solve_in_kl(
    proba_map: ProbaMap,
    prior_param: ProbaParam,
    direction: np.ndarray,
    kl_max: float,
    alpha_max: float,
    y_pres=None,
    x_pres=None,
    m_max=100,
) -> float:
    """
    Find largest alpha < alpha_max such that kl(prior_param + alpha *dir, prior_param) < kl_max

    Done by dichotomy.

    Note:
        Getting the largest alpha might not be preferable depending on the nature of the mapping.
    """

    ### Aims at solving proba_map.kl( proba_map.to_param(), post_param)
    def loc_fun(alpha):
        try:
            new_prior_param = prior_param + alpha * direction
            return proba_map.kl(new_prior_param, prior_param)
        except RenormError:
            return np.inf

    # implement solver for loc_fun = kl_max, assuming loc_fun is increasing in alpha.
    # Use dichotomy, take lower value

    if loc_fun(alpha_max) < kl_max:
        return alpha_max

    return dichoto(
        loc_fun,
        kl_max,
        0,
        alpha_max,
        increasing=True,
        y_pres=y_pres,
        x_pres=x_pres,
        m_max=m_max,
    )[0]


def _solve_in_kl_pre_exp(
    proba_map: PreExpFamily,
    prior_param: ProbaParam,
    direction: np.ndarray,
    kl_max: float,
    alpha_max: float,
    y_pres=None,
    x_pres=None,
    m_max=100,
) -> float:
    """
    Find largest alpha < alpha_max such that kl(prior_param + alpha *dir, prior_param) < kl_max

    Done by dichotomy.

    Note:
        Getting the largest alpha might not be preferable depending on the nature of the mapping.
    """

    ### Aims at solving proba_map.kl( proba_map.to_param(), post_param)
    t_prior_param = proba_map.param_to_T(prior_param)

    def loc_fun(alpha):
        try:
            new_prior_param = proba_map.T_to_param(t_prior_param + alpha * direction)
            return proba_map.kl(new_prior_param, prior_param)
        except RenormError:
            return np.inf

    # implement solver for loc_fun = kl_max, assuming loc_fun is increasing in alpha.
    # Use dichotomy, take lower value

    if loc_fun(alpha_max) < kl_max:
        return alpha_max

    return dichoto(
        loc_fun,
        kl_max,
        0,
        alpha_max,
        increasing=True,
        y_pres=y_pres,
        x_pres=x_pres,
        m_max=m_max,
    )[0]


class MetaLearningEnv:
    r"""Meta Learning environment for Variational Catoni PAC Bayes

    For a collection of task, meta learns a suitable prior.

    Class attributes:
    - proba_map: A ProbaMap instance, defining the shared family of probabilities in which the meta
    prior is learnt, and in which the tasks' posterior live.
    - list_tasks: A list of Task objects. All tasks should share the same parameter space, coherent
    with the proba_map attribute (this is not checked, training will fail).
    - prior_param: ProbaParam, containing the current prior parameter.
    - hyperparams: dictionary, containing hyperparameters for training each task.
    - hist_meta: HistMeta, track the evolution of score and prior_param during training
    - n_task: int, the number of tasks
    - task_score: the list of task end penalised score
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
    defined as
        $$S(\theta_0)
        = \sum_i \pi(\hat{\theta}_i)[R_i] + \lambda_i KL(\pi(\hat{\theta}_i), \pi(\theta_0))$$

    The derivative of the meta score has simple expression $\sum \lambda_i K_i$ where $K_i$ is the
    gradient of the Kullback--Leibler term $KL(\pi(\hat{\theta}_i), \pi(\theta_0))$ with respect to
    $\theta_0$ at fixed $\hat{\theta}_i$ value.
    """

    def __init__(
        self,
        proba_map: ProbaMap,
        list_task: list[Task],
        prior_param: Optional[ProbaParam] = None,
        eta:float = 0.01,
        kl_max: float = 1.0,
        kl_cond_type: Union[str, int] = 0,
        kl_tol:float = 10**-3,
        hyperparams : Optional[dict] = None,
    ):
        """Initialize meta learning environnement.

        Args:
            proba_map (ProbaMap): class of distributions on which priors/posterior are optimized
            list_task (list[Task]): list of learning task constituing the meta learning
                environnement.
            prior_param (ProbaParam): initial prior param. Optional, default to ref_param in
                proba_map.
            eta (float): Meta Gradient step size during training
            kl_max (float): Maximum KL step size between prior and posterior during training
                (type of KL depends on kl_cond_type)
            kl_cond_type (str or float): Type of KL condition considered.
            hyperparams (dict): further arguments passed to pacbayes_minimize (inner learning
                algorithm).
        """

        self.proba_map = proba_map

        self.list_task = list_task
        self.task_score = np.full(len(list_task), np.inf)  # inf since not known
        self.n_task = len(list_task)

        if prior_param is None:
            prior_param = proba_map.ref_param
        self.prior_param = prior_param
        self.meta_score = None

        self.eta = eta
        self.kl_max = kl_max
        self.kl_cond_type = kl_cond_type

        self.kl_tol = kl_tol
 
        if hyperparams is None:
            self.hyperparams = {}
        else:
            self.hyperparams = hyperparams

        if "per_step" not in self.hyperparams:
            # Current rule of thumb: at least twice the dimension of the meta parameter
            # This field is prepared since we need it to initialize the accu length.
            # Future versions should have variable 'per_step' argument.
            self.hyperparams["per_step"] = min(100, 2 * prod(proba_map.proba_param_shape))

        if "optimizer" not in self.hyperparams:
            self.hyperparams["optimizer"] = None

        self.hyperparams["optimizer"] = infer_pb_routine(
            proba_map=proba_map, pac_bayes_solver=hyperparams["optimizer"]
        )

        self.hist_meta = HistMeta(
            meta_param_shape=proba_map.proba_param_shape, n=1, n_task=self.n_task
        )
        self.hist_meta.add1(prior_param, np.nan, self.task_score)  # type: ignore
        self.converged = False

        # initialize accu for each task
        if hyperparams["optimizer"].accu_type == FunEvalsExp:

            def init_accu(task: Task):
                if task.accu_sample_val is None:
                    task.accu_sample_val = FunEvalsExp(
                        sample_shape=proba_map.sample_shape,
                        t_shape=proba_map.t_shape,  # type: ignore
                        n_tot=1,
                    )

        elif hyperparams["optimizer"].accu_type == FunEvalsDens:

            def init_accu(task: Task):
                if task.accu_sample_val is None:
                    task.accu_sample_val = FunEvalsDens(
                        sample_shape=proba_map.sample_shape,
                        n_tot=1,
                    )

        elif hyperparams["optimizer"].accu_type == FunEvalsDens:

            def init_accu(task: Task):
                if task.accu_sample_val is None:
                    task.accu_sample_val = FunEvals(
                        sample_shape=proba_map.sample_shape,
                        n_tot=1,
                    )

        else:
            warnings.warn(
                f"""Could not interpret {hyperparams['optimizer']}.
                Trying to use it as FunEvals"""
            )

            def init_accu(task: Task):
                if task.accu_sample_val is None:
                    task.accu_sample_val = hyperparams["optimizer"](
                        sample_shape=proba_map.sample_shape,
                        n_tot=1,
                    )

        # Inplace intialisation of field accu_sample_val for each task if missing
        for task in self.list_task:
            init_accu(task)

        # Choose space in which gradients are computed
        # If considering an exponentialy family with a parametrisation other than
        # the natural parametrisation, still perform gradient descent in the natural
        # parametrisation IF KL gradients can be efficiently computed in the natural
        # parametrisation (i.e. if grad_g is implemented).
        if isinstance(proba_map, PreExpFamily):
            if proba_map.grad_g is not None:
                self.work_in_t = True
            else:
                self.work_in_t = False
        else:
            self.work_in_t = False

    def _mk_loc_hyperparams(self, hyperparams: Optional[dict] = None) -> dict:
        """Locally update stored hyperparameters using new hyperparameters"""
        loc_hyperparams = self.hyperparams.copy()
        if hyperparams is not None:
            loc_hyperparams.update(hyperparams)
        return loc_hyperparams

    def _extend_memo(self, task: Task, epochs: int, hyperparams: Optional[dict] = None):
        """Extend memory of accu for a task depending on hyperparameters and number
        of epochs"""
        loc_hyperparams = self._mk_loc_hyperparams(hyperparams)
 
        n_remain = task.accu_sample_val.n_remain()  # type: ignore
        per_step = loc_hyperparams["per_step"]
        if isinstance(per_step, int):
            chain_length = loc_hyperparams.get("chain_length", 10)
            n_fill = epochs * per_step * chain_length
 
        elif isinstance(per_step, list):
            chain_length = self.hyperparams.get("chain_length", None)
            if chain_length is None:
                n_fill = epochs * np.sum(per_step)
            else:
                n_fill = epochs * np.sum(per_step[:chain_length])
        else:
            # Could not extend, this will be done at each task call
            return
        if n_fill < n_remain:
            task.accu_sample_val.extend_memory(n_fill - n_remain)  # type: ignore
 

    def train(self, task: Task, hyperparams:Optional[dict] = None) -> None:
        """Perform inner learning for a task using learning environnement prior.

        "post_param" and "accu_sample_val" are updated inplace in the task.

        The inner algorithm called is 'aduq.bayes.pacbayes_minimize.' The routine used depends
        on the proba_map and hyperparams attributes of the learning environnement (pre inferred
        at construction time).

        The 'accu_sample_val' field of the task is indirectly augmented by pacbayes_minimize.

        Args:
            task: the task which should be trained (i.e. score function, tempertaure, accu_sample_val)
        **kwargs:
            passed to pacbayes_minimize

        Outputs:
            None (the task post_param, end_score and accu_sample_val attributes are modified)
        """
        train_updt_hyperparams = task.train_hyperparams.copy()
        train_updt_hyperparams.update(hyperparams)
        loc_hyperparams = self._mk_loc_hyperparams(train_updt_hyperparams)

        # Perform the inner algorithm
        opt_res = pacbayes_minimize(
            fun=task.score,
            proba_map=self.proba_map,
            prior_param=self.prior_param,
            post_param=task.post_param,
            temperature=task.temp,
            prev_eval=task.accu_sample_val,
            vectorized=task.vectorized,
            parallel=task.parallel,
            **loc_hyperparams,
        )

        # Store output in task
        task.post_param = opt_res.opti_param
        task.end_score = opt_res.opti_score  # type: ignore

    def grad_meta(
        self, task: Task, n_grad_KL: int = 10**4, hyperparams: Optional[dict] = None
    ) -> ProbaParam:
        """Compute the meta gradient for a provided task.
 
        Arg:
            task: a Task object.
            n_grad_KL: number of samples generated to compute the KL gradient
 
        Output:
            The gradient of the penalised meta score with respect to prior_param.
        """
        # Perform the inner algorithm
        self.train(task, hyperparams=hyperparams)
 
        # Compute the gradient of the meta parameter as temp * nabla_2 KL(post, prior)
        if not self.work_in_t:
            return (
                task.temp
                * self.proba_map.grad_right_kl(task.post_param)(  # type: ignore
                    self.prior_param, n_grad_KL
                )[0]
            )
        else:
            return task.temp * (
                self.proba_map.der_g(self.proba_map.param_to_T(self.prior_param))
                - self.proba_map.der_g(self.proba_map.param_to_T(task.post_param))
            )

    def _init_grad(self):
        """Construct an accu for the gradient (array full of 0 of adequate shape)"""
        if self.work_in_t:
            return np.zeros(self.proba_map.t_shape)
        return np.zeros(self.proba_map.proba_param_shape)

    def _get_eta_use(self, grad:np.ndarray)->float:
        """Compute eta satisfying the condition on KL between new prior and current prior
        Handles whether computations should be performed on natural parametrisation or
        default parametrisation of the proba_map
 
        Args:
            grad: gradient
        returns:
            largest float eta such that KL(prior - eta * grad, prior) < limit
            AND eta < eta_max
        """
        return EnforceKL(
            proba_map=self.proba_map,
            prior_param=self.prior_param,
            direction=-grad,
            kl_max=self.kl_max,
            alpha_max=self.eta,
            work_in_t=self.work_in_t,
            kl_type=self.kl_cond_type).enforce()

    def _get_new_prior_param(self, eta_use: float, grad: np.ndarray) -> ProbaParam:
        """Compute new prior parameter from local eta value and gradient as
            'prior_param - eta_use * grad'
        Handles whether computations should be performed on the natural parametrisation
        or on the default parametrisation
        """
        if self.work_in_t:
            return self.proba_map.T_to_param(
                self.proba_map.param_to_T(self.prior_param) - eta_use * grad
            )
        return self.prior_param - eta_use * grad
 
    def new_prior_param_from_grad(self, grad: np.ndarray) -> ProbaParam:
        """Compute new prior from gradient.
 
        The update is:
            "prior - eta_use * grad"
        where eta_use is the largest eta < eta_max such that KL distance between new prior
        and current prior (KL(new, old)) is less than kl_max.
 
        Handles whether computations should be performed on the natural parametrisation
        or on the default parametrisation of the space."""
        eta_use = self._get_eta_use(grad)
        return self._get_new_prior_param(eta_use, grad)

    def meta_learn(
        self,
        epochs: int = 1,
        mini_batch_size:int = 10,
        hyperparams: Optional[dict] = None,
        silent: bool = False,
    ) -> None:
        """Meta Learning algorithm

        Args:
            epochs (int): number of learning epochs (default 1)
            eta (float): step size for gradient descent (default 0.01)
            silent (bool): should there be any print

        Outputs:
            None (modifications inplace)

        The tasks are read one after another and the prior is updated after each task is read.
        """
        # Extend history for meta learning log
        self.hist_meta.extend_memory(epochs)

        # Extend memory for tasks (once and for all rather than iteratively)
        for task in self.list_task:
            self._extend_memo(task, epochs, hyperparams)

        batch_count = (self.n_task // mini_batch_size) + ((self.n_task % mini_batch_size) > 0)

        # Main learning loop
        for i in range(epochs):
            blab(silent, f"Iteration {i}/{epochs}")

            permut = np.random.permutation(self.n_task)

            for n_batch in range(batch_count):
                blab(silent, f"Starting minibatch {n_batch + 1} / {batch_count}")
                grad = self._init_grad()
                start = mini_batch_size * n_batch
                iloc_task_s = permut[start:(start * mini_batch_size)]
                    
                # Iterate over tasks
                for j, iloc_task in enumerate(iloc_task_s):
                    blab(silent, f"Starting task {iloc_task} ({start+j+i}/{self.n_task})")

                    # Compute gradient (this updates task posterior automatically)
                    task = self.list_task[iloc_task]
                    grad += self.grad_meta(task, hyperparams=hyperparams)

                    # Store end score for task
                    self.task_score[iloc_task] = task.end_score

                grad = grad / len(iloc_task_s)

                blab(silent, f"Minibatch {n_batch+1} avg score: {self.task_score[iloc_task_s].mean()}")

                self.prior_param = self.new_prior_param_from_grad(grad)

                blab(silent)

            # Log meta learning result
            self.meta_score = np.mean(self.task_score)
            self.hist_meta.add1(self.prior_param, self.meta_score, self.task_score)

            blab(silent, f"Meta score: {self.meta_score}\n")

    def meta_learn_batch(
        self,
        epochs: int = 1,
        hyperparams: Optional[dict]=None,
        silent: bool = False,
    ):
        """
        Meta Learning algorithm (batch variant)

        Args:
            epochs (int): number of learning epochs (default 1)
            eta (float): step size for gradient descent (default 0.01)
            kl_tol (float): convergence criteria for posterior param. Default 10**-3.
            kl_max (float): maximum step size between a prior and its update. Default np.inf
            silent (bool): should prints be silenced?

        Outputs:
            None (modifications inplace)

        The prior is updated after all tasks have been read. Improves stability at the cost of
        duration (for the early stages) compared to non batch version.
        """
        # Extend history for meta learning log
        self.hist_meta.extend_memory(epochs)

        # Extend memory for tasks (once and for all rather than iteratively)
        for task in self.list_task:
            self._extend_memo(task, epochs, hyperparams)

        # Set up convergence and loop
        converged = False
        i = 0

        # Main learning loop
        while (i < epochs) and (not converged):
            blab(silent, f"Iteration {i}/{epochs}")


            grad = self._init_grad()

            # Iterate over tasks
            for j, task in enumerate(self.list_task):
                blab(silent, f"Starting task {j+1}/{self.n_task}")
                # Compute gradient (this updates task posterior automatically)
                grad = grad + self.grad_meta(task, hyperparams=hyperparams)
                # Store end score for task
                self.task_score[j] = task.end_score

            grad = grad / self.n_task

            # Compute effective step size (prevents KL(new_prior, prior)> kl_max)
            new_prior_param = self.new_prior_param_from_grad(grad)

            # Check convergence
            delta_kl = self.proba_map.kl(new_prior_param, self.prior_param)
            converged = delta_kl < self.kl_tol
            i += 1

            # Log/update meta learning result
            self.prior_param = new_prior_param
            self.meta_score = np.mean(self.task_score)
            self.hist_meta.add1(self.prior_param, self.meta_score, self.task_score)

            blab(silent, f"Meta score: {self.meta_score}\n")

        # Check convergence
        if converged:
            self.converged = True
            blab(silent, "Algorithm converged")

    def save(self, name: str, path: str = ".", overwrite: bool = False) -> str:
        """
        Save FunEvals object to folder 'name' situated at 'path' (default to working folder)
        """
        if not os.path.isdir(path):
            raise ValueError(f"{path} should point to a folder")
        acc_path = os.path.join(path, name)
        os.makedirs(acc_path, exist_ok=overwrite)

        # Save hyperparams information
        with open(os.path.join(acc_path, "hyperparams.dl"), "wb") as file:
            dill.dump(self.hyperparams, file)

        # Save proba_map (TO DO: check whether this impact inference of type)
        with open(os.path.join(acc_path, "proba_map.dl"), "wb") as file:
            dill.dump(self.proba_map, file)

        # Save tasks
        tasks_path = os.path.join(acc_path, "tasks")
        os.makedirs(tasks_path, exist_ok=overwrite)

        for i, task in enumerate(self.list_task):
            task.save(f"task_{i}", tasks_path, overwrite=overwrite)

        # Save HistMeta
        self.hist_meta.save("hist_meta", acc_path, overwrite=overwrite)

        # Save converged
        with open(
            os.path.join(acc_path, "converged.txt"), "w", encoding="utf-8"
        ) as file:
            file.write(str(self.converged))

        return acc_path

class MetaLearningEnvAdam(MetaLearningEnv):
    r"""Meta Learning environment for Variational Catoni PAC Bayes using Adam solver

    For a collection of task, meta learns a suitable prior.

    Class attributes:
    - proba_map: A ProbaMap instance, defining the shared family of probabilities in which the meta
    prior is learnt, and in which the tasks' posterior live.
    - list_tasks: A list of Task objects. All tasks should share the same parameter space, coherent
    with the proba_map attribute (this is not checked, training will fail).
    - prior_param: ProbaParam, containing the current prior parameter.
    - hyperparams: dictionary, containing hyperparameters for training each task.
    - hist_meta: HistMeta, track the evolution of score and prior_param during training
    - n_task: int, the number of tasks
    - task_score: the list of task end penalised score
    - converged: boolean, specifying if convergence has been reached
    - meta_score: float, the current meta score for the prior
    - adamizer: Adamizer, manages Adam solver

    Routine motivation:
    In the context of penalised risk minimisation inner algorithm, the meta gradient is easy to
    compute (see below). As such, the meta training algorithm is a Gradient descent procedure. To
    improve stability, the prior distribution is forced to evolve slowly (in term of KL divergence)

    Gradient of the meta score for Catoni Pac-Bayes.
    For a proba map $\pi$, noting $\theta_0$ the prior parameter, $R_i$, $\lambda_i$ the score
    function and temperature for task $i$, $\hat{\theta}_i = \hat{\theta}_i(\theta_0)$ the
    posterior parameter using prior $\theta_0$, the meta score of prior parameter $\theta_0$ is
    defined as
        $$S(\theta_0)
        = \sum_i \pi(\hat{\theta}_i)[R_i] + \lambda_i KL(\pi(\hat{\theta}_i), \pi(\theta_0))$$

    The derivative of the meta score has simple expression $\sum \lambda_i K_i$ where $K_i$ is the
    gradient of the Kullback--Leibler term $KL(\pi(\hat{\theta}_i), \pi(\theta_0))$ with respect to
    $\theta_0$ at fixed $\hat{\theta}_i$ value.

    NOTE:
        MetaLearningEnv already has an 'eta' variable which is redundant with Adamizer 'alpha'
        variable. Therefore the 'alpha' variable is set to 1.
    """
    def __init__(
        self,
        proba_map: ProbaMap,
        list_task: list[Task],
        prior_param: Optional[ProbaParam] = None,
        eta: float = 0.01,
        beta1: float = 0.9,
        beta2: float = 0.99,
        epsilon: float = 1e-8,
        kl_max: float = 1.0,
        kl_cond_type: Union[str, int] = 0,
        kl_tol=10**-3,
        hyperparams: Optional[dict] = None,
    ):
        # Create the Adam solver manager
        self.adamizer = Adamizer(alpha=1.0, beta1=beta1, beta2=beta2, epsilon=epsilon)

        super().__init__(
            proba_map=proba_map,
            list_task=list_task,
            prior_param=prior_param,
            eta=eta,
            kl_max=kl_max,
            kl_cond_type=kl_cond_type,
            kl_tol=kl_tol,
            hyperparams=hyperparams,
        )
 
    def new_prior_param_from_grad(self, grad: np.ndarray) -> ProbaParam:
        """Compute new prior from gradient using adam update rule"""
        direction = self.adamizer.comp_updt(gradient=grad)
 
        eta_use = self._get_eta_use(-direction)
        return self._get_new_prior_param(eta_use, -direction)