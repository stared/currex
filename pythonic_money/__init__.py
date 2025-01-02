from forex_python.converter import CurrencyRates
from decimal import Decimal
from typing import Union, Optional
import functools


class Currency:
    _rates = CurrencyRates()

    def __init__(self, amount: Union[int, float, Decimal], code: str):
        self.amount = Decimal(str(amount))
        self.code = code

    def __mul__(self, other):
        if isinstance(other, (int, float, Decimal)):
            return type(self)(self.amount * Decimal(str(other)))
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        return f"{self.amount:.2f} {self.code}"

    def __repr__(self):
        return f"{self.code}({self.amount})"


def _currency_factory(code: str) -> type:
    """Creates a new currency class for the given currency code."""

    @functools.wraps(Currency)
    def __init__(self, amount: Union[int, float, Decimal] = 1):
        super(type(self), self).__init__(amount, code)

    def __call__(cls, other: Currency) -> "Currency":
        if isinstance(other, Currency):
            rate = cls._rates.get_rate(other.code, code)
            return cls(other.amount * Decimal(str(rate)))
        raise TypeError(f"Cannot convert {type(other)} to {code}")

    return type(
        code, (Currency,), {"__init__": __init__, "__call__": classmethod(__call__)}
    )


# Create currency classes
USD = _currency_factory("USD")
EUR = _currency_factory("EUR")
GBP = _currency_factory("GBP")
PLN = _currency_factory("PLN")
JPY = _currency_factory("JPY")
CHF = _currency_factory("CHF")

__all__ = ["USD", "EUR", "GBP", "PLN", "JPY", "CHF"]
