import requests
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
    _api_url = "https://hexarate.paikama.co/api/rates/latest"
    _rates_cache = {}

    @classmethod
    def _get_rate(cls, from_currency: str, to_currency: str) -> Decimal:
        """Get exchange rate from Hexarate API"""
        cache_key = f"{from_currency}-{to_currency}"
        if cache_key in cls._rates_cache:
            return cls._rates_cache[cache_key]

        try:
            response = requests.get(
                f"{cls._api_url}/{from_currency}", params={"target": to_currency}
            )
            response.raise_for_status()
            data = response.json()
            if data["status_code"] != 200:
                raise ValueError(f"API returned error status: {data['status_code']}")
            rate = Decimal(str(data["data"]["mid"]))
            cls._rates_cache[cache_key] = rate
            return rate
        except Exception as e:
            raise ValueError(f"Failed to get exchange rate: {str(e)}")

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

        from_currency = self.__class__.__name__
        to_currency = currency_class.__name__

        rate = self._get_rate(from_currency, to_currency)
        converted_amount = self.amount * rate
        return currency_class(converted_amount)


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
