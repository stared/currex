from forex_python.converter import CurrencyRates
from decimal import Decimal
from typing import Union, Optional
import functools


class CurrencyMeta(type):
    def __mul__(cls, other):
        if isinstance(other, (int, float, Decimal)):
            return cls(Decimal(str(other)))
        return NotImplemented

    def __rmul__(cls, other):
        if isinstance(other, (int, float, Decimal)):
            return cls(Decimal(str(other)))
        return NotImplemented


class Currency(metaclass=CurrencyMeta):
    _rates = CurrencyRates()

    def __init__(self, amount: Union[int, float, Decimal]):
        self.amount = Decimal(str(amount))

    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return type(self)(self.amount * Decimal(str(other)))
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"{self.amount:.2f} {self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.amount})"

    def to(self, currency_class: type) -> "Currency":
        """Convert to another currency"""
        if not issubclass(currency_class, Currency):
            raise TypeError(f"Cannot convert to {currency_class}")

        try:
            rate = self._rates.get_rate(
                self.__class__.__name__, currency_class.__name__
            )
            return currency_class(self.amount * Decimal(str(rate)))
        except Exception as e:
            raise ValueError(f"Failed to get exchange rate: {str(e)}")


def _currency_factory(code: str) -> type:
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
