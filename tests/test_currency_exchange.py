import pytest
from currex import USD, EUR, GBP, PLN
from decimal import Decimal


@pytest.mark.exchange
def test_usd_to_eur_conversion():
    """Test USD to EUR conversion"""
    usd_amount = 100 * USD
    eur_amount = EUR(usd_amount)
    assert isinstance(eur_amount, EUR)
    assert eur_amount.amount > 0


@pytest.mark.exchange
def test_eur_to_pln_conversion():
    """Test EUR to PLN conversion"""
    eur_amount = 50 * EUR
    pln_amount = PLN(eur_amount)
    assert isinstance(pln_amount, PLN)
    assert pln_amount.amount > 0


@pytest.mark.exchange
def test_round_trip_conversion():
    """Test converting back and forth between currencies"""
    original = 100 * USD
    converted = EUR(original)
    back_to_usd = USD(converted)

    # Due to exchange rate fluctuations and rounding,
    # we check if the value is within 1% of original
    assert abs(back_to_usd.amount - original.amount) / original.amount < Decimal("0.01")


@pytest.mark.exchange
def test_multi_currency_chain():
    """Test converting through multiple currencies"""
    start_amount = 100 * USD
    # USD -> EUR -> GBP -> PLN
    result = PLN(GBP(EUR(start_amount)))
    assert isinstance(result, PLN)
    assert result.amount > 0


@pytest.mark.exchange
def test_comparison_different_currencies():
    """Test comparisons between different currencies (requires exchange rates)"""
    amount_pln = 100 * PLN
    amount_eur = 100 * EUR

    # Assuming 1 EUR is always worth more than 1 PLN
    assert amount_pln < amount_eur
    assert amount_pln <= amount_eur