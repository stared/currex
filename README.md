# Pythonic Money

A Pythonic currency calculator that makes working with currencies and exchange rates simple and intuitive.

## Installation

```bash
pip install pythonic-money
```

## Usage

```python
from pythonic_money import *

# Convert 100 USD to EUR
result = EUR(100 * USD)
print(result)  # Prints the amount in EUR

# Convert British Pounds to Polish Złoty
pln_amount = PLN(23.4 * GBP)
print(pln_amount)  # Prints the amount in PLN
```

## Features

- Real-time exchange rates
- Intuitive Pythonic API
- Support for major world currencies
- Automatic currency conversion
- Type-safe operations

## Requirements

- Python 3.10 or higher
- Internet connection for real-time exchange rates

## License

MIT License
