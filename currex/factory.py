from typing import Type
from .currency import Currency


def _currency_factory(code: str) -> Type[Currency]:
    """Creates a new currency class for the given currency code."""

    class NewCurrency(Currency):
        pass

    NewCurrency.__name__ = code
    return NewCurrency


# Create currency classes
USD = _currency_factory("USD")
EUR = _currency_factory("EUR")
GBP = _currency_factory("GBP")
PLN = _currency_factory("PLN")
JPY = _currency_factory("JPY")
CHF = _currency_factory("CHF")

__all__ = ["USD", "EUR", "GBP", "PLN", "JPY", "CHF"]
