"""Gradient enhancer abstract base class
A gradient enhancer transforms a standard gradient descent approach into
an "enhanced" gradient descent (e.g. Nesterov momentum, adam).
All memory management should be dealt with in the gradient enhancer.

One method only is mandatory: comp_updt, which takes as input a gradient,
and returns the update rule, i.e. the step which should be added to the param.
Convention is that the new param will be
    new param = old param + step
"""

from abc import ABC, abstractmethod

class GradientEnhancer(ABC):
    """Gradient enhancer abstract base class
    A gradient enhancer transforms a standard gradient descent approach into
    an "enhanced" gradient descent (e.g. Nesterov momentum, adam).
    All memory management should be dealt with in the gradient enhancer.

    One method only is mandatory: comp_updt, which takes as input a gradient,
    and returns the update rule, i.e. the step which should be added to the param.
    Convention is that the new param will be
        new param = old param + step
    """

    @abstractmethod
    def comp_updt(self, gradient):
        pass

