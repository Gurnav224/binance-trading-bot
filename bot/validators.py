def validate_input(symbol, side, order_type, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT pairs allowed")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT order")

    # optional but strong
    if price and quantity * price < 100:
        raise ValueError("Order must be at least $100")