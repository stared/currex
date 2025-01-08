# Currex

[![currex version - PyPI](https://img.shields.io/pypi/v/currex)](https://pypi.org/project/currex/)
![PyPI status](https://img.shields.io/pypi/status/currex.svg)
![MIT license - PyPI](https://img.shields.io/pypi/l/currex.svg)
![Python version - PyPI](https://img.shields.io/pypi/pyversions/currex.svg)
[![GitHub Actions: Build](https://img.shields.io/github/actions/workflow/status/stared/currex/test.yml?branch=main)](https://github.com/stared/currex/actions)
[![GitHub Actions: Linting](https://img.shields.io/github/actions/workflow/status/stared/currex/lint.yml?branch=main&label=linting)](https://github.com/stared/currex/actions)
[![Twitter @pmigdal](https://img.shields.io/twitter/follow/pmigdal)](https://twitter.com/pmigdal)

A Pythonic currency calculator that makes working with currencies and exchange rates simple and smooth - by [Piotr Migdał](https://p.migdal.pl/).

I often use Python as a command-line calculator. Yet, I need to go back to Google Search to convert between currencies. So, for my own convenience, I created this library that makes it easy to add, multiply and change currencies. One of the core features is autocasting - when using a few currencies, automatically convert them to the first one.

It is intended to be used in interactive Python sessions (such as Jupyter Notebook, IPython, etc.) to get ballpark estimates of prices - e.g. when traveling, buying online, etc. Personally, I use it from the command line IPython.

It is a new package, so I'm open to suggestions.

It is **NOT intended to be used in production code**. Every API design decision I made was to make it as simple as possible to use in interactive sessions. Some of them are consciously at odds with a tool that could be used in a library.

**EVEN MORE IMPORTANT**: Never use it for any important decisions - taxes, investments, etc. There is no guarantee that the exchange rates are up-to-date and correct. Note that even major players make mistakes, e.g. [Google Glitch Undervalues Poland's Zloty By A Fifth](https://www.barrons.com/news/google-glitch-undervalues-poland-s-zloty-by-a-fifth-b4d695e7). Always use the official exchange rates.

## Installation

```bash
pip install currex
```

## Usage

```python
from currex import *

# use currencies as if they were numbers
100 * USD  # USD(100.00)
12 * USD(100)  # USD(1200.00)

# convert currencies to other currencies
USD(100).to(EUR)  # EUR(85.30)
USD(100).to(PLN)  # PLN(430.50)

# this syntax is also supported
PLN(EUR(12))  # PLN(51.33)

# add different currencies
USD(100) + EUR(100)  # USD(203.42)
EUR(100) - USD(100)  # EUR(3.22)

# divide currencies
USD(2) / JPY(14)  # 22.531428526365715

# configure decimal digits (default is 2)
currex_config.set_decimal_digits(3)  # show 3 decimal places
USD(123.456789)  # USD(123.457)
currex_config.set_decimal_digits(None)  # show full precision
USD(123.456789)  # USD(123.456789)
```

## Features

- Arithmetic operations with currencies
- Currency conversion
- Autocasting - when using a few currencies, automatically convert them to the first one
- Configurable decimal places for currency representation

## Requirements

- Python 3.9 or higher
- Internet connection for real-time exchange rates - it uses [HexaRate](https://hexarate.paikama.co/)

## TODO

- Mock API for testing
- More backends for exchange rates
- Support for more cryptocurrencies

## License

MIT License by [Piotr Migdał](https://p.migdal.pl/)
