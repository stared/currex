from decimal import Decimal

import pytest

from currex import USD, currex_config


def test_basic_multiplication():
    amount = 100 * USD
    assert isinstance(amount, USD)
    assert amount.amount == Decimal("100")

    amount = USD * 100
    assert isinstance(amount, USD)
    assert amount.amount == Decimal("100")


def test_basic_division():
    amount = USD(100) / 2
    assert isinstance(amount, USD)
    assert amount.amount == Decimal("50")


def test_addition():
    amount1 = 100 * USD
    amount2 = 50 * USD
    total = amount1 + amount2
    assert isinstance(total, USD)
    assert total.amount == Decimal("150")


def test_subtraction():
    amount1 = 100 * USD
    amount2 = 30 * USD
    diff = amount1 - amount2
    assert isinstance(diff, USD)
    assert diff.amount == Decimal("70")


def test_comparison():
    # Same currency comparisons
    amount1 = 100 * USD
    amount2 = 50 * USD
    amount3 = 100 * USD

    assert amount1 > amount2
    assert amount2 < amount1
    assert amount1 >= amount3
    assert amount1 <= amount3
    assert amount1 == amount3
    assert amount1 != amount2


def test_string_representation():
    amount = 42.42 * USD
    assert str(amount).endswith("USD")
    assert "42.42" in str(amount)


def test_negative_amounts():
    amount = -50 * USD
    assert amount.amount == Decimal("-50")

    amount2 = 30 * USD
    result = amount + amount2
    assert result.amount == Decimal("-20")


def test_zero_amount():
    amount = 0 * USD
    assert amount.amount == Decimal("0")


def test_decimal_digits_configuration():
    """Test the decimal digits configuration for currency representation."""
    amount = USD(123.456789)

    # Default (2 digits)
    assert str(amount) == "123.46 USD"
    assert repr(amount) == "USD(123.46)"

    # Change to 3 digits
    currex_config.set_decimal_digits(3)
    assert str(amount) == "123.457 USD"
    assert repr(amount) == "USD(123.457)"

    # Change to no rounding (None)
    currex_config.set_decimal_digits(None)
    assert str(amount) == "123.456789 USD"
    assert repr(amount) == "USD(123.456789)"

    # Reset to default
    currex_config.set_decimal_digits(2)
    assert str(amount) == "123.46 USD"
    assert repr(amount) == "USD(123.46)"


def test_invalid_decimal_digits():
    """Test that negative decimal digits raise ValueError."""
    with pytest.raises(ValueError):
        currex_config.set_decimal_digits(-1)
