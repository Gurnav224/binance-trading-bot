from bot.client import BinanceClient

client = BinanceClient()

def place_order(symbol, side, order_type, quantity, price=None):
    params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity,
    }

    if order_type == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    return client.create_order(**params)


def get_final_order_status(symbol, order_id):
    return client.get_order(symbol, order_id)