r"""
brent-search package
====================

Brent's method for univariate function optimization.

Functions
---------

bracket   Find a bracketing interval.
brent     Seeks a local minimum of a function via Brent's method.
minimize  Function minimization.
test      Test this package.
"""

from ._bracket import bracket
from ._brent import brent
from ._optimize import minimize
from ._testit import test

__version__ = "2.0.2"

__all__ = ["__version__", "test", "bracket", "brent", "minimize"]
