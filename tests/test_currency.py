import pytest
from currex import USD, EUR, GBP, PLN
from decimal import Decimal


def test_basic_multiplication():
    amount = 100 * USD
    assert isinstance(amount, USD)
    assert amount.amount == Decimal("100")


def test_currency_conversion():
    usd_amount = 100 * USD
    eur_amount = EUR(usd_amount)
    assert isinstance(eur_amount, EUR)
    assert eur_amount.amount > 0


def test_chained_operations():
    # Convert 50 EUR to PLN
    pln_amount = PLN(50 * EUR)
    assert isinstance(pln_amount, PLN)
    assert pln_amount.amount > 0


def test_string_representation():
    amount = 42.42 * USD
    assert str(amount).endswith("USD")
    assert "42.42" in str(amount)
