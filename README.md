# Currex

A Pythonic currency calculator that makes working with currencies and exchange rates simple and intuitive.

Works best in interactive python sessions (Jupyter Notebook, IPython, etc.).

## Installation

```bash
pip install git+https://github.com/stared/currex.git
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
EUR(100) + USD(100)  # EUR(196.6100)

# divide currencies
USD(2) / JPY(14)  # 22.531428526365715
```

## Features

- Real-time exchange rates
- Intuitive Pythonic API
- Support for major world currencies
- Automatic currency conversion
- Type-safe operations

## Requirements

- Python 3.10 or higher
- Internet connection for real-time exchange rates - it uses [HexaRate](https://hexarate.paikama.co/)

## License

MIT License
