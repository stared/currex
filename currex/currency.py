from decimal import Decimal
from typing import Union, Type, TypeVar
from .exchange import ExchangeRateAPI

DecimalLike = Union[int, float, Decimal]
C = TypeVar("C", bound="Currency")


def to_decimal(value: DecimalLike) -> Decimal:
    """Convert a DecimalLike value to Decimal"""
    return value if isinstance(value, Decimal) else Decimal(str(value))


class CurrencyMeta(type):
    def __mul__(cls: Type[C], other: DecimalLike) -> C:
        return cls(to_decimal(other))

    def __rmul__(cls: Type[C], other: DecimalLike) -> C:
        return cls(to_decimal(other))


class Currency(metaclass=CurrencyMeta):
    def __init__(self, amount: Union["Currency", DecimalLike]):
        if isinstance(amount, Currency):
            converted = amount.to(type(self))
            self.amount = converted.amount
        else:
            self.amount = to_decimal(amount)

    def __mul__(self: C, other: DecimalLike) -> C:
        return type(self)(self.amount * to_decimal(other))

    def __rmul__(self: C, other: DecimalLike) -> C:
        return self.__mul__(other)

    def __add__(self: C, other: Union["Currency", DecimalLike]) -> C:
        if isinstance(other, Currency):
            converted = other.to(type(self))
            return type(self)(self.amount + converted.amount)
        return type(self)(self.amount + to_decimal(other))

    def __radd__(self: C, other: DecimalLike) -> C:
        return type(self)(self.amount + to_decimal(other))

    def __neg__(self: C) -> C:
        """Return the negative of this currency amount"""
        return type(self)(-self.amount)

    def __sub__(self: C, other: Union["Currency", DecimalLike]) -> C:
        """Subtract another currency (with conversion) or decimal-like number"""
        if isinstance(other, Currency):
            converted = other.to(type(self))
            return type(self)(self.amount - converted.amount)
        return type(self)(self.amount - to_decimal(other))

    def __rsub__(self: C, other: DecimalLike) -> C:
        """Subtract this currency from a decimal-like number"""
        return type(self)(to_decimal(other) - self.amount)

    def __truediv__(self, other: Union["Currency", DecimalLike]) -> Union[C, float]:
        """Divide by another currency (returns unitless) or decimal-like number (returns same currency)"""
        if isinstance(other, Currency):
            converted = other.to(type(self))
            return float(self.amount / converted.amount)
        return type(self)(self.amount / to_decimal(other))

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
