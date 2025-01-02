from decimal import Decimal
from typing import Union, Type, TypeVar
from .exchange import ExchangeRateAPI

DecimalLike = Union[int, float, Decimal]
C = TypeVar("C", bound="Currency")


class CurrencyMeta(type):
    def __mul__(cls: Type[C], other: DecimalLike) -> C:
        return cls(Decimal(str(other)))

    def __rmul__(cls: Type[C], other: DecimalLike) -> C:
        return cls(Decimal(str(other)))


class Currency(metaclass=CurrencyMeta):
    def __init__(self, amount: Union["Currency", DecimalLike]):
        if isinstance(amount, DecimalLike):
            self.amount = Decimal(str(amount))
        else:
            converted = amount.to(type(self))
            self.amount = converted.amount

    def __mul__(self: C, other: DecimalLike) -> C:
        return type(self)(self.amount * Decimal(str(other)))

    def __rmul__(self: C, other: DecimalLike) -> C:
        return self.__mul__(other)

    def __add__(self: C, other: Union["Currency", DecimalLike]) -> C:
        if isinstance(other, Currency):
            converted = other.to(type(self))
            return type(self)(self.amount + converted.amount)
        return type(self)(self.amount + Decimal(str(other)))

    def __radd__(self: C, other: DecimalLike) -> C:
        return type(self)(self.amount + Decimal(str(other)))

    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.__class__.__name__}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.amount})"

    def to(self, currency_class: Type[C]) -> C:
        """Convert to another currency"""
        from_currency = self.__class__.__name__
        to_currency = currency_class.__name__

        rate = ExchangeRateAPI.get_rate(from_currency, to_currency)
        converted_amount = self.amount * rate
        return currency_class(converted_amount)
