from decimal import Decimal

import requests


class ExchangeRateAPI:
    _api_url: str = "https://hexarate.paikama.co/api/rates/latest"
    _rates_cache: dict[str, Decimal] = {}

    @classmethod
    def get_rate(cls, from_currency: str, to_currency: str) -> Decimal:
        """Get exchange rate from Hexarate API"""
        cache_key = f"{from_currency}-{to_currency}"
        if cache_key in cls._rates_cache:
            return cls._rates_cache[cache_key]

        try:
            response = requests.get(
                f"{cls._api_url}/{from_currency}", params={"target": to_currency}
            )
            response.raise_for_status()
            data = response.json()
            if data["status_code"] != 200:
                raise ValueError(f"API returned error status: {data['status_code']}")
            rate = Decimal(str(data["data"]["mid"]))
            cls._rates_cache[cache_key] = rate
            return rate
        except Exception as e:
            raise ValueError(f"Failed to get exchange rate: {str(e)}") from e
