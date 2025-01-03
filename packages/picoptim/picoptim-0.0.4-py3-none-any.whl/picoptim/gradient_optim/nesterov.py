from picoptim.gradient_optim.gradient_optimizer import GradientOptimizer
from picoptim.gradient_optim.gradient_enhancer import GradientEnhancer
import numpy as np

from typing import Optional, Callable

class Nesterovizer(GradientEnhancer):
    def __init__(self, momentum:float=0.95):
        self.momentum = momentum

        self.v = 0
        
    def comp_updt(self, gradient):
        self.v = self.momentum * self.v - (1- self.momentum) * gradient
        return self.v


class NesterovSolver(GradientOptimizer):
    def __init__(
        self,
        fun_with_gradient: Callable[[np.ndarray], float],
        param_ini:np.ndarray,
        eta:float = 1.0,
        # Termination criteria
        chain_length: int = 10**3,
        xtol: float = 10 ** (-8),
        ftol: float = 10 ** (-8),
        delta_conv_check: int = 1,
        # Function evaluation
        kwargs: Optional[dict] = None,
        parallel:bool = False,
        vectorized:bool=False,
        # Adam hyperparameters
        momentum:float = 0.9,
        # Printing
        silent: bool = False,
        print_rec : int = 5,
    ):
    
        self.nesterov = Nesterovizer(momentum=momentum)

        super().__init__(
            fun_with_gradient=fun_with_gradient,
            param_ini=param_ini,
            eta=eta,
            chain_length=chain_length,
            xtol=xtol,
            ftol=ftol,
            delta_conv_check=delta_conv_check,
            kwargs=kwargs,
            parallel=parallel,vectorized=vectorized,
            silent=silent,
            print_rec=print_rec
            )
        


    def update_param(self, grad):
        """Update parameter using Nesterov Momentum"""
        self.param += self.nesterov.comp_updt(grad)
