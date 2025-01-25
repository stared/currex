from decimal import Decimal
from typing import Union

from .config import currex_config
from .exchange import ExchangeRateAPI

DecimalLike = Union[int, float, Decimal]


def to_decimal(value: DecimalLike) -> Decimal:
    """Convert a DecimalLike value to Decimal"""
    return value if isinstance(value, Decimal) else Decimal(str(value))


class Currency:
    """A currency with an amount and a code."""

    def __init__(self, code: str, amount: DecimalLike = 1) -> None:
        """Initialize a currency with a code and optional amount.

        Args:
            code: The currency code (e.g. 'USD', 'EUR', 'PLN')
            amount: The amount in the currency (defaults to 1)
        """
        self.code = code
        self.amount = to_decimal(amount)

    def __call__(self, amount: Union["Currency", DecimalLike]) -> "Currency":
        """Syntactic sugar for creating currency amounts or converting between currencies.

        This enables syntax like:
            PLN(100)  # 100 PLN
            PLN(USD(50))  # Convert 50 USD to PLN

        Args:
            amount: Either a number (creates new amount in this currency) or
                   another Currency (converts to this currency)
        """
        if isinstance(amount, Currency):
            return amount.to(self.code)
        return Currency(self.code, amount)

    def __mul__(self, other: DecimalLike) -> "Currency":
        return Currency(self.code, self.amount * to_decimal(other))

    def __rmul__(self, other: DecimalLike) -> "Currency":
        return self.__mul__(other)

    def __add__(self, other: Union["Currency", DecimalLike]) -> "Currency":
        if isinstance(other, Currency):
            converted = other.to(self.code)
            return Currency(self.code, self.amount + converted.amount)
        return Currency(self.code, self.amount + to_decimal(other))

    def __radd__(self, other: DecimalLike) -> "Currency":
        return Currency(self.code, self.amount + to_decimal(other))

    def __neg__(self) -> "Currency":
        """Return the negative of this currency amount"""
        return Currency(self.code, -self.amount)

    def __sub__(self, other: Union["Currency", DecimalLike]) -> "Currency":
        """Subtract another currency (with conversion) or decimal-like number"""
        if isinstance(other, Currency):
            converted = other.to(self.code)
            return Currency(self.code, self.amount - converted.amount)
        return Currency(self.code, self.amount - to_decimal(other))

    def __rsub__(self, other: DecimalLike) -> "Currency":
        """Subtract this currency from a decimal-like number"""
        return Currency(self.code, to_decimal(other) - self.amount)

    def __truediv__(self, other: Union["Currency", DecimalLike]) -> Union["Currency", float]:
        """Divide by another currency (returns unitless) or decimal-like number
        (returns same currency)"""
        if isinstance(other, Currency):
            converted = other.to(self.code)
            return float(self.amount / converted.amount)
        return Currency(self.code, self.amount / to_decimal(other))

    def __eq__(self, other: object) -> bool:
        """Equal only if same currency type and amount"""
        if not isinstance(other, Currency):
            return NotImplemented
        return self.code == other.code and self.amount == other.amount

    def __ne__(self, other: object) -> bool:
        """Not equal if different currency type or amount"""
        if not isinstance(other, Currency):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: "Currency") -> bool:
        """Less than, converts other currency if needed"""
        if not isinstance(other, Currency):
            return NotImplemented
        if self.code != other.code:
            other = other.to(self.code)
        return self.amount < other.amount

    def __le__(self, other: "Currency") -> bool:
        """Less than or equal, converts other currency if needed"""
        if not isinstance(other, Currency):
            return NotImplemented
        if self.code != other.code:
            other = other.to(self.code)
        return self.amount <= other.amount

    def __gt__(self, other: "Currency") -> bool:
        """Greater than, converts other currency if needed"""
        if not isinstance(other, Currency):
            return NotImplemented
        if self.code != other.code:
            other = other.to(self.code)
        return self.amount > other.amount

    def __ge__(self, other: "Currency") -> bool:
        """Greater than or equal, converts other currency if needed"""
        if not isinstance(other, Currency):
            return NotImplemented
        if self.code != other.code:
            other = other.to(self.code)
        return self.amount >= other.amount

    def __str__(self) -> str:
        digits = currex_config.get_decimal_digits()
        if digits is None:
            return f"{self.amount} {self.code}"
        return f"{self.amount:.{digits}f} {self.code}"

    def __repr__(self) -> str:
        digits = currex_config.get_decimal_digits()
        if digits is None:
            return f"{self.code}({self.amount})"
        return f"{self.code}({self.amount:.{digits}f})"

    def to(self, currency: Union[str, "Currency"]) -> "Currency":
        """Convert to another currency"""
        if isinstance(currency, str):
            currency_code = currency
        else:
            currency_code = currency.code

        if self.code == currency_code:
            return Currency(self.code, self.amount)

        rate = ExchangeRateAPI.get_rate(self.code, currency_code)
        converted_amount = self.amount * rate
        return Currency(currency_code, converted_amount)
