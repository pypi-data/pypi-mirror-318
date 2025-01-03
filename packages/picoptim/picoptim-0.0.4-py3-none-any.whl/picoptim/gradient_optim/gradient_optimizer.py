from picoptim.optimizer import IterOptimizer

import numpy as np
from typing import Optional, Callable

def get_first_output(fun):
    def mod_fun(*args, **kwargs):
        return fun(*args, **kwargs)[0]
    return mod_fun

class GradientOptimizer(IterOptimizer):
    """Vanilla Gradient Descent implementation"""
    def __init__(
        self,
        fun_with_gradient: Callable[[np.ndarray], float],
        param_ini: np.ndarray,
        # Gradient method parameters
        eta:float,
        # Termination criteria
        chain_length: int,
        xtol: float = 10 ** (-8),
        ftol: float = 10 ** (-8),
        delta_conv_check: int = 1,
        # Function evaluation
        kwargs: Optional[dict] = None,
        parallel: bool = False,
        vectorized: bool = False,
        # Printing
        silent: bool = False,
        print_rec: int = 5,
    ):
        super().__init__(
            fun = get_first_output(fun_with_gradient),
            param_ini=param_ini,
            chain_length=chain_length,
            xtol=xtol,
            ftol=ftol,
            delta_conv_check=delta_conv_check,
            kwargs=kwargs,
            parallel=parallel,
            vectorized=vectorized,
            silent=silent,
            print_rec=print_rec)
        self.fun_with_grad= fun_with_gradient
        self.eta = eta

    def update_param(self, grad):
        """Update parameter from gradient (inplace)
        Update rule is 
            param = param - eta * grad
        """
        self.param -= self.eta * grad

    def update(self):
        """Update rule for Gradient Descent."""
        self.score, grad = self.fun_with_grad(self.param)
        self.update_param(grad)
        super().update()
