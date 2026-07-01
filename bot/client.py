from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.config import API_KEY, API_SECRET
from bot.exceptions import ConfigurationError, BinanceClientError


class BinanceClient:

    def __init__(self):

        if not API_KEY or not API_SECRET:
            raise ConfigurationError(
                "API Key or Secret not found in .env"
            )

        self.client = Client(
            api_key=API_KEY,
            api_secret=API_SECRET,
            testnet=True
        )

        # Force Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def test_connection(self):
        """
        Test if Binance is reachable.
        """
        try:
            self.client.futures_ping()
            return True

        except BinanceAPIException as e:
            raise BinanceClientError(e.message)

        except Exception as e:
            raise BinanceClientError(str(e))
        

    def place_order(self, **kwargs):
        try:
            return self.client.futures_create_order(**kwargs)

        except BinanceAPIException as e:
            raise BinanceClientError(e.message)

        except Exception as e:
            raise BinanceClientError(str(e))