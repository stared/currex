"""Configuration module for currex."""

from typing import Optional


class CurrexConfig:
    _decimal_digits: Optional[int] = 2

    @classmethod
    def set_decimal_digits(cls, digits: Optional[int]) -> None:
        """Set the number of decimal digits for currency representation.

        Args:
            digits: Number of decimal digits to display. Use None for full precision.
        """
        if digits is not None and digits < 0:
            raise ValueError("Number of decimal digits cannot be negative")
        cls._decimal_digits = digits

    @classmethod
    def get_decimal_digits(cls) -> Optional[int]:
        """Get the current number of decimal digits setting."""
        return cls._decimal_digits


# Create a global instance for easy access
currex_config = CurrexConfig()
