"""Currency factory module."""

from .currency import Currency

# Create currency instances for all supported currencies
CURRENCIES = [
    "USD",  # United States Dollar
    "EUR",  # Euro
    "GBP",  # British Pound Sterling
    "JPY",  # Japanese Yen
    "CHF",  # Swiss Franc
    "AUD",  # Australian Dollar
    "CAD",  # Canadian Dollar
    "CNY",  # Chinese Yuan
    "HKD",  # Hong Kong Dollar
    "NZD",  # New Zealand Dollar
    "SEK",  # Swedish Krona
    "KRW",  # South Korean Won
    "SGD",  # Singapore Dollar
    "NOK",  # Norwegian Krone
    "MXN",  # Mexican Peso
    "INR",  # Indian Rupee
    "RUB",  # Russian Ruble
    "ZAR",  # South African Rand
    "TRY",  # Turkish Lira
    "BRL",  # Brazilian Real
    "TWD",  # New Taiwan Dollar
    "DKK",  # Danish Krone
    "PLN",  # Polish Złoty
    "THB",  # Thai Baht
    "IDR",  # Indonesian Rupiah
    "CZK",  # Czech Koruna
    "AED",  # UAE Dirham
    "AFN",  # Afghan Afghani
    "AOA",  # Angolan Kwanza
    "ARS",  # Argentine Peso
    "BAM",  # Bosnia-Herzegovina Convertible Mark
    "BGN",  # Bulgarian Lev
    "BYN",  # Belarusian Ruble
    "CDF",  # Congolese Franc
    "CLP",  # Chilean Peso
    "COP",  # Colombian Peso
    "CUP",  # Cuban Peso
    "GEL",  # Georgian Lari
    "GHS",  # Ghanaian Cedi
    "GNF",  # Guinean Franc
    "HUF",  # Hungarian Forint
    "ILS",  # Israeli New Shekel
    "ISK",  # Icelandic Króna
    "KZT",  # Kazakhstani Tenge
    "MDL",  # Moldovan Leu
    "MGA",  # Malagasy Ariary
    "MRU",  # Mauritanian Ouguiya
    "MZN",  # Mozambican Metical
    "NIO",  # Nicaraguan Córdoba
    "PEN",  # Peruvian Sol
    "PHP",  # Philippine Peso
    "PKR",  # Pakistani Rupee
    "RON",  # Romanian Leu
    "RSD",  # Serbian Dinar
    "SDG",  # Sudanese Pound
    "SRD",  # Surinamese Dollar
    "STN",  # São Tomé and Príncipe Dobra
    "TJS",  # Tajikistani Somoni
    "TMT",  # Turkmenistani Manat
    "UAH",  # Ukrainian Hryvnia
    "UGX",  # Ugandan Shilling
    "UYU",  # Uruguayan Peso
    "UZS",  # Uzbekistani Som
    "VES",  # Venezuelan Bolívar Soberano
    "XAF",  # CFA Franc BEAC
    "XOF",  # CFA Franc BCEAO
    "ZMW",  # Zambian Kwacha
]

# Create currency instances and add them to globals
for code in CURRENCIES:
    globals()[code] = Currency(code)

__all__ = ["Currency"] + CURRENCIES
