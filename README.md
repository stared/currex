# Currex

[![currex version - PyPI](https://img.shields.io/pypi/v/currex)](https://pypi.org/project/currex/)
![PyPI status](https://img.shields.io/pypi/status/currex.svg)
![MIT license - PyPI](https://img.shields.io/pypi/l/currex.svg)
![Python version - PyPI](https://img.shields.io/pypi/pyversions/currex.svg)
[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/stared/currex/test.yml?branch=main)](https://github.com/stared/currex/actions)
[![Twitter @pmigdal](https://img.shields.io/twitter/follow/pmigdal)](https://twitter.com/pmigdal)

A Pythonic currency calculator that makes working with currencies and exchange rates simple and smooth.

I often use Python as a command-line calculator. Yet, I need to go back to Google Search to convert between curriencies. So, for my own convenience, I created this library.

It is inteded to be used interactive python sessions (such as Jupyter Notebook, IPython, etc.) to get ballpark estimates of prices - e.g. when travelling, buying online, etc.

It is NOT intended to be used in production code. Every API design decision I made was to make it as simple as possible to use it in interactive sessions.

**EVEN MORE IMPORTANT**: Never use it for any important decisions - taxes, investments, etc. There is not quarantee that the exchange rates are correct.

## Installation

```bash
pip install currex
```

## Usage

```python
from currex import *

# use currencies as if they were numbers
100 * USD  # USD(100)
12 * USD(100)  # USD(1200)

# convert currencies to other currencies
USD(100).to(EUR)  # EUR(85.3)
USD(100).to(PLN)  # PLN(430.5)

# this syntax is also supported
PLN(EUR(12))  # PLN(51.3312)

# add different currencies
USD(100) + EUR(100)  # USD(203.50500)
EUR(100) - USD(100)  # EUR(2.60500)

# divide currencies
USD(2) / JPY(14)  # 22.531428526365715
```

## Features

- Arithmetic operations with currencies
- Currency conversion
- Autocasting - when using a few currencies, automatically convert them to the first one

## Requirements

- Python 3.10 or higher
- Internet connection for real-time exchange rates - it uses [HexaRate](https://hexarate.paikama.co/)

## TODO

- Installation with PyPI
- Mock API for testing
- More backends for exchange rates

## License

MIT License by [Piotr Migdał](https://p.migdal.pl/)
