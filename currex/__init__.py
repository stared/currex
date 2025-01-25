"""
Currex - A Python library for currency conversion and arithmetic
"""

from .config import currex_config
from .currency import Currency
from .exchange import ExchangeRateAPI
from .factory import *  # noqa: F403
from .factory import CURRENCIES

__version__ = "0.1.2"
__all__ = ["Currency", "ExchangeRateAPI", "currex_config"] + CURRENCIES
