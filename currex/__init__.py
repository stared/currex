"""
Currex - A Python library for currency conversion and arithmetic
"""

from .currency import Currency
from .factory import USD, EUR, GBP, PLN, JPY, CHF
from .exchange import ExchangeRateAPI

__version__ = "0.1.0"
__all__ = ["Currency", "USD", "EUR", "GBP", "PLN", "JPY", "CHF", "ExchangeRateAPI"]
