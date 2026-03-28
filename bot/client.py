from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

class BinanceClient:
    def __init__(self):
        self.client = Client(
            os.getenv("API_KEY"),
            os.getenv("API_SECRET"),
            testnet=True
        )

    def create_order(self, **params):
        return self.client.futures_create_order(**params)

    def get_order(self, symbol, order_id):
        return self.client.futures_get_order(
            symbol=symbol,
            orderId=order_id
        )