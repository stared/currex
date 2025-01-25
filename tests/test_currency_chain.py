"""Tests for currency chain conversions.

This test file verifies that we can convert between pairs of currencies
by converting 1 unit of currency at index 2n to currency at index 2n+1.
"""

import pytest

from currex import CURRENCIES, Currency


@pytest.mark.api
def test_specific_currency_pairs():
    """Test some specific currency pairs that are commonly used."""
    test_cases = [
        (Currency("USD", 1), "EUR"),  # USD to EUR
        (Currency("EUR", 1), "GBP"),  # EUR to GBP
        (Currency("GBP", 1), "JPY"),  # GBP to JPY
        (Currency("CHF", 1), "CAD"),  # CHF to CAD
        (Currency("AUD", 1), "SGD"),  # AUD to SGD
    ]

    for amount, target_currency in test_cases:
        converted = amount.to(target_currency)
        assert converted.code == target_currency
        assert converted.amount > 0, (
            f"Converting 1 {amount.code} to {target_currency} " "resulted in 0 or negative amount"
        )


@pytest.mark.api
def test_currency_conversion_all():
    """Test converting 1 unit between pairs of currencies."""
    # Convert 1 unit from currency at index 2n to currency at index 2n+1
    for i in range(0, len(CURRENCIES) - 1, 2):
        from_currency_code = CURRENCIES[i]
        to_currency_code = CURRENCIES[i + 1]

        # Create amount of 1 in the source currency
        amount = Currency(from_currency_code, 1)

        # Convert to target currency
        converted = amount.to(to_currency_code)

        # Verify the conversion produced a valid result
        assert converted.code == to_currency_code
        assert converted.amount > 0, (
            f"Converting 1 {from_currency_code} to {to_currency_code} "
            "resulted in 0 or negative amount"
        )
