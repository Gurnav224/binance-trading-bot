import click
import time
import logging

from bot.orders import place_order, get_final_order_status
from bot.validators import validate_input
from bot.logging_config import setup_logger

setup_logger()


@click.command()
@click.option('--symbol', required=True)
@click.option('--side', required=True)
@click.option('--type', 'order_type', required=True)
@click.option('--qty', required=True, type=float)
@click.option('--price', required=False, type=float)

def main(symbol, side, order_type, qty, price):
    try:
        # ✅ Validation
        validate_input(symbol, side, order_type, qty, price)

        print("\n📌 Order Request")
        print("-------------------------")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {qty}")
        print(f"Price    : {price if price else 'MARKET'}")

        # ✅ Place Order
        res = place_order(symbol, side, order_type, qty, price)

        logging.info(f"Order Request: {symbol} {side} {order_type} {qty} {price}")
        logging.info(f"Initial Response: {res}")

        # ⏳ Wait and fetch final status
        time.sleep(2)
        updated = get_final_order_status(symbol, res["orderId"])

        logging.info(f"Final Response: {updated}")

        print("\n📊 Final Order Result")
        print("-------------------------")
        print(f"Order ID     : {updated.get('orderId')}")
        print(f"Status       : {updated.get('status')}")
        print(f"Executed Qty : {updated.get('executedQty')}")
        print(f"Avg Price    : {updated.get('avgPrice')}")

        print("\n✅ Done")

    except Exception as e:
        logging.error(str(e))
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()