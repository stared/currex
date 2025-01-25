# Currex

[![currex version - PyPI](https://img.shields.io/pypi/v/currex)](https://pypi.org/project/currex/)
![PyPI status](https://img.shields.io/pypi/status/currex.svg)
![MIT license - PyPI](https://img.shields.io/pypi/l/currex.svg)
![Python version - PyPI](https://img.shields.io/pypi/pyversions/currex.svg)
[![GitHub Actions: Build](https://img.shields.io/github/actions/workflow/status/stared/currex/test.yml?branch=main)](https://github.com/stared/currex/actions)
[![GitHub Actions: Linting](https://img.shields.io/github/actions/workflow/status/stared/currex/lint.yml?branch=main&label=linting)](https://github.com/stared/currex/actions)
[![Twitter @pmigdal](https://img.shields.io/twitter/follow/pmigdal)](https://twitter.com/pmigdal)

A Pythonic currency calculator that makes working with currencies and exchange rates simple and smooth - by [Piotr Migdał](https://p.migdal.pl/). [See it in action in Colab](https://colab.research.google.com/github/stared/currex/blob/main/currex.ipynb) - no need to install anything.

I often use Python as a command-line calculator. However, I frequently found myself going back to Google Search to convert between currencies. So, I created this library to make it easy to add, multiply, and convert between currencies. One of its core features is autocasting - when working with multiple currencies, it automatically converts them to match the first currency used.

This library is designed for use in interactive Python sessions (such as Jupyter Notebook, Jupyter Lab, or IPython) to quickly get ballpark price estimates - perfect for travel planning or online shopping. I personally use it through IPython on the command line.

Right now it uses [HexaRate](https://hexarate.paikama.co/) for exchange rates.

It is a new package, so [I'm open to suggestions](https://github.com/stared/currex/issues).

## Disclaimer

It is **NOT intended to be used in production code**. Every API design decision was made to optimize for interactive sessions. Some decisions consciously go against best practices for production libraries. For example, the main namespace defines all currencies as constants, and the example code uses `from currex import *` - practices I believe are appropriate for interactive sessions only.

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

For a slightly more advanced use, there is a general `Currency` class:

```python
from currex import Currency

USD = Currency("USD")  # one dollar

money = Currency("USD", 100)  # USD(100.00)
money.to("EUR")  # EUR(95.30)
```

## Features

- Arithmetic operations with currencies
- Currency conversion
- Autocasting - when using a few currencies, automatically convert them to the first one
- Configurable decimal places for currency representation

## Requirements

- Python 3.9 or higher
- Internet connection for real-time exchange rates

## Development

To set up the development environment:

```bash
git clone git@github.com:stared/currex.git
cd currex
pip install -e .[dev]
```

## TODO

- Mock API for testing
- More backends for exchange rates, see [e.g. this list](https://publicapis.dev/category/currency-exchange)
- Support for cryptocurrencies

## License

MIT License by [Piotr Migdał](https://p.migdal.pl/)
