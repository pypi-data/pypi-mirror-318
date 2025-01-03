"""Adam Gradient Descent procedure (https://arxiv.org/abs/1412.6980 )"""

from picoptim.gradient_optim.gradient_optimizer import GradientOptimizer
from picoptim.gradient_optim.gradient_enhancer import GradientEnhancer
import numpy as np

from typing import Optional, Callable


class Adamizer(GradientEnhancer):
    def __init__(
        self,
        alpha:float = 0.001,
        beta1:float = 0.9,
        beta2:float = 0.99,
        epsilon:float = 1e-8):
        self.alpha = alpha
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

        self.beta1t = self.beta1
        self.beta2t = self.beta2

        # Abuse numpy multiplication/ addition rules
        self.m = 0.0
        self.v = 0.0


    def updt_beta_t(self):
        self.beta1t = self.beta1t * self.beta1
        self.beta2t = self.beta2t * self.beta2

    def dgrd_beta_(self):
        self.beta1t = self.beta1t / self.beta1
        self.beta2t = self.beta2t / self.beta2

    def comp_updt(self, gradient):
        self.m = self.beta1 * self.m + (1- self.beta1) * gradient
        self.v = self.beta2 * self.v + (1 - self.beta2) * (gradient **2)

        m_hat = self.m / (1 - self.beta1t)
        v_hat = self.v / (1 - (self.beta2t))

        return - self.alpha * m_hat / (np.sqrt(v_hat) + self.epsilon)
        
    

class AdamSolver(GradientOptimizer):
    def __init__(
        self,
        fun_with_gradient: Callable[[np.ndarray], float],
        param_ini:np.ndarray,
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
        alpha:float=0.001,
        beta1:float=0.9,
        beta2:float=0.99,
        epsilon: float = 1e-8,
        # Printing
        silent: bool = False,
        print_rec : int = 5,
    ):
    
        self.adamizer = Adamizer(alpha, beta1, beta2, epsilon)

        super().__init__(
            fun_with_gradient=fun_with_gradient,
            param_ini=param_ini,
            eta=alpha,
            chain_length=chain_length,
            xtol=xtol,
            ftol=ftol,
            delta_conv_check=delta_conv_check,
            kwargs=kwargs,
            parallel=parallel,vectorized=vectorized,
            silent=silent,
            print_rec=print_rec
            )
        
    @property
    def eta(self):
        """Eta value (stored in adamizer)"""
        return self.adamizer.alpha

    @eta.setter
    def eta(self, value):
        self.adamizer.alpha = value

    def update_param(self, grad):
        self.param += self.adamizer.comp_updt(grad)
