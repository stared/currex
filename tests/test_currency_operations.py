import pytest
from currex import USD, EUR, GBP, PLN
from decimal import Decimal


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
