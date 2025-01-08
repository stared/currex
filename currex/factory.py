from typing import Type

from .currency import Currency


def _currency_factory(code: str) -> Type[Currency]:
    """Creates a new currency class for the given currency code."""

    class NewCurrency(Currency):
        pass

    NewCurrency.__name__ = code
    return NewCurrency


# Create currency classes for major currencies
USD = _currency_factory("USD")  # United States Dollar
EUR = _currency_factory("EUR")  # Euro
GBP = _currency_factory("GBP")  # British Pound Sterling
JPY = _currency_factory("JPY")  # Japanese Yen
CHF = _currency_factory("CHF")  # Swiss Franc
AUD = _currency_factory("AUD")  # Australian Dollar
CAD = _currency_factory("CAD")  # Canadian Dollar
CNY = _currency_factory("CNY")  # Chinese Yuan
HKD = _currency_factory("HKD")  # Hong Kong Dollar
NZD = _currency_factory("NZD")  # New Zealand Dollar
SEK = _currency_factory("SEK")  # Swedish Krona
KRW = _currency_factory("KRW")  # South Korean Won
SGD = _currency_factory("SGD")  # Singapore Dollar
NOK = _currency_factory("NOK")  # Norwegian Krone
MXN = _currency_factory("MXN")  # Mexican Peso
INR = _currency_factory("INR")  # Indian Rupee
RUB = _currency_factory("RUB")  # Russian Ruble
ZAR = _currency_factory("ZAR")  # South African Rand
TRY = _currency_factory("TRY")  # Turkish Lira
BRL = _currency_factory("BRL")  # Brazilian Real
TWD = _currency_factory("TWD")  # New Taiwan Dollar
DKK = _currency_factory("DKK")  # Danish Krone
PLN = _currency_factory("PLN")  # Polish Złoty
THB = _currency_factory("THB")  # Thai Baht
IDR = _currency_factory("IDR")  # Indonesian Rupiah
CZK = _currency_factory("CZK")  # Czech Koruna
AED = _currency_factory("AED")  # UAE Dirham
AFN = _currency_factory("AFN")  # Afghan Afghani
AOA = _currency_factory("AOA")  # Angolan Kwanza
ARS = _currency_factory("ARS")  # Argentine Peso
BAM = _currency_factory("BAM")  # Bosnia-Herzegovina Convertible Mark
BGN = _currency_factory("BGN")  # Bulgarian Lev
BYN = _currency_factory("BYN")  # Belarusian Ruble
CDF = _currency_factory("CDF")  # Congolese Franc
CLP = _currency_factory("CLP")  # Chilean Peso
COP = _currency_factory("COP")  # Colombian Peso
CUP = _currency_factory("CUP")  # Cuban Peso
GEL = _currency_factory("GEL")  # Georgian Lari
GHS = _currency_factory("GHS")  # Ghanaian Cedi
GNF = _currency_factory("GNF")  # Guinean Franc
HUF = _currency_factory("HUF")  # Hungarian Forint
ILS = _currency_factory("ILS")  # Israeli New Shekel
ISK = _currency_factory("ISK")  # Icelandic Króna
KZT = _currency_factory("KZT")  # Kazakhstani Tenge
MDL = _currency_factory("MDL")  # Moldovan Leu
MGA = _currency_factory("MGA")  # Malagasy Ariary
MRU = _currency_factory("MRU")  # Mauritanian Ouguiya
MZN = _currency_factory("MZN")  # Mozambican Metical
NIO = _currency_factory("NIO")  # Nicaraguan Córdoba
PEN = _currency_factory("PEN")  # Peruvian Sol
PHP = _currency_factory("PHP")  # Philippine Peso
PKR = _currency_factory("PKR")  # Pakistani Rupee
RON = _currency_factory("RON")  # Romanian Leu
RSD = _currency_factory("RSD")  # Serbian Dinar
SDG = _currency_factory("SDG")  # Sudanese Pound
SRD = _currency_factory("SRD")  # Surinamese Dollar
STN = _currency_factory("STN")  # São Tomé and Príncipe Dobra
TJS = _currency_factory("TJS")  # Tajikistani Somoni
TMT = _currency_factory("TMT")  # Turkmenistani Manat
UAH = _currency_factory("UAH")  # Ukrainian Hryvnia
UGX = _currency_factory("UGX")  # Ugandan Shilling
UYU = _currency_factory("UYU")  # Uruguayan Peso
UZS = _currency_factory("UZS")  # Uzbekistani Som
VES = _currency_factory("VES")  # Venezuelan Bolívar Soberano
XAF = _currency_factory("XAF")  # CFA Franc BEAC
XOF = _currency_factory("XOF")  # CFA Franc BCEAO
ZMW = _currency_factory("ZMW")  # Zambian Kwacha

# Update __all__ to include all currency classes
__all__ = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CHF",
    "AUD",
    "CAD",
    "CNY",
    "HKD",
    "NZD",
    "SEK",
    "KRW",
    "SGD",
    "NOK",
    "MXN",
    "INR",
    "RUB",
    "ZAR",
    "TRY",
    "BRL",
    "TWD",
    "DKK",
    "PLN",
    "THB",
    "IDR",
    "CZK",
    "AED",
    "AFN",
    "AOA",
    "ARS",
    "BAM",
    "BGN",
    "BYN",
    "CDF",
    "CLP",
    "COP",
    "CUP",
    "GEL",
    "GHS",
    "GNF",
    "HUF",
    "ILS",
    "ISK",
    "KZT",
    "MDL",
    "MGA",
    "MRU",
    "MZN",
    "NIO",
    "PEN",
    "PHP",
    "PKR",
    "RON",
    "RSD",
    "SDG",
    "SRD",
    "STN",
    "TJS",
    "TMT",
    "UAH",
    "UGX",
    "UYU",
    "UZS",
    "VES",
    "XAF",
    "XOF",
    "ZMW",
]
