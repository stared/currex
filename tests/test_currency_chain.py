"""Tests for currency chain conversions.

This test file verifies that we can convert between pairs of currencies
by converting 1 unit of currency at index 2n to currency at index 2n+1.
"""

import pytest
from currex import (
    USD,
    EUR,
    GBP,
    JPY,
    CHF,
    AUD,
    CAD,
    HKD,
    NZD,
    SEK,
    KRW,
    SGD,
    NOK,
    MXN,
    INR,
    RUB,
    ZAR,
    TRY,
    BRL,
    TWD,
    DKK,
    PLN,
    THB,
    IDR,
    CZK,
    AED,
    AFN,
    AOA,
    ARS,
    BAM,
    BGN,
    BYN,
    CDF,
    CLP,
    COP,
    CUP,
    GEL,
    GHS,
    GNF,
    HUF,
    ILS,
    ISK,
    KZT,
    MDL,
    MGA,
    MRU,
    MZN,
    NIO,
    PEN,
    PHP,
    PKR,
    RON,
    RSD,
    SDG,
    SRD,
    STN,
    TJS,
    TMT,
    UAH,
    UGX,
    UYU,
    UZS,
    VES,
    XAF,
    XOF,
    ZMW,
)


@pytest.mark.api
def test_specific_currency_pairs():
    """Test some specific currency pairs that are commonly used."""
    test_cases = [
        (USD(1), EUR),  # USD to EUR
        (EUR(1), GBP),  # EUR to GBP
        (GBP(1), JPY),  # GBP to JPY
        (CHF(1), CAD),  # CHF to CAD
        (AUD(1), SGD),  # AUD to SGD
    ]

    for amount, target_currency in test_cases:
        converted = amount.to(target_currency)
        assert isinstance(converted, target_currency)
        assert (
            converted.amount > 0
        ), f"Converting 1 {amount.__class__.__name__} to {target_currency.__name__} resulted in 0 or negative amount"
        print(f"1 {amount.__class__.__name__} = {converted}")


@pytest.mark.api
def test_currency_conversion_all():
    """Test converting 1 unit between pairs of currencies."""
    # Create a list of all currency classes
    currencies = [
        USD,
        EUR,
        GBP,
        JPY,
        CHF,
        AUD,
        CAD,
        HKD,
        NZD,
        SEK,
        KRW,
        SGD,
        NOK,
        MXN,
        INR,
        RUB,
        ZAR,
        TRY,
        BRL,
        TWD,
        DKK,
        PLN,
        THB,
        IDR,
        CZK,
        AED,
        AFN,
        AOA,
        ARS,
        BAM,
        BGN,
        BYN,
        CDF,
        CLP,
        COP,
        CUP,
        GEL,
        GHS,
        GNF,
        HUF,
        ILS,
        ISK,
        KZT,
        MDL,
        MGA,
        MRU,
        MZN,
        NIO,
        PEN,
        PHP,
        PKR,
        RON,
        RSD,
        SDG,
        SRD,
        STN,
        TJS,
        TMT,
        UAH,
        UGX,
        UYU,
        UZS,
        VES,
        XAF,
        XOF,
        ZMW,
    ]

    # Convert 1 unit from currency at index 2n to currency at index 2n+1
    for i in range(0, len(currencies) - 1, 2):
        from_currency = currencies[i]
        to_currency = currencies[i + 1]

        # Create amount of 1 in the source currency
        amount = from_currency(1)

        # Convert to target currency
        converted = amount.to(to_currency)

        # Verify the conversion produced a valid result
        assert isinstance(converted, to_currency)
        assert (
            converted.amount > 0
        ), f"Converting 1 {from_currency.__name__} to {to_currency.__name__} resulted in 0 or negative amount"

        print(f"1 {from_currency.__name__} = {converted}")
