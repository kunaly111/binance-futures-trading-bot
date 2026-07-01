import click

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.exceptions import ValidationError, BinanceClientError


@click.command()
def main():

    try:
        # -----------------------------
        # Take User Input
        # -----------------------------
        symbol = click.prompt("Trading Symbol", type=str)
        side = click.prompt("Side (BUY/SELL)", type=str)
        order_type = click.prompt("Order Type (MARKET/LIMIT)", type=str)
        quantity = click.prompt("Quantity", type=float)

        price = None

        # Ask price only for LIMIT orders
        if order_type.upper() == "LIMIT":
            price = click.prompt("Price", type=float)

        # -----------------------------
        # Validation
        # -----------------------------
        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(price, order_type)

        # -----------------------------
        # Order Summary
        # -----------------------------
        print("\n" + "=" * 50)
        print("ORDER REQUEST")
        print("=" * 50)

        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if order_type == "LIMIT":
            print(f"Price      : {price}")

        print("=" * 50)

        # -----------------------------
        # Place Order
        # -----------------------------
        if order_type == "MARKET":
            response = place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        else:
            response = place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        # -----------------------------
        # Success Output
        # -----------------------------
        print("\n✅ ORDER PLACED SUCCESSFULLY\n")

        print("=" * 50)
        print("ORDER RESPONSE")
        print("=" * 50)

        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Average Price : {response.get('avgPrice', 'N/A')}")

        print("=" * 50)

    except ValidationError as e:
        print(f"\n❌ Validation Error: {e}")

    except BinanceClientError as e:
        print(f"\n❌ Binance Error: {e}")

    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")


if __name__ == "__main__":
    main()