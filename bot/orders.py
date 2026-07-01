from binance.enums import (
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
)

from bot.client import BinanceClient
from bot.logging_config import logger

# Create a single Binance client instance
client = BinanceClient()


def place_market_order(symbol, side, quantity):
    """
    Place a MARKET order.
    """

    logger.info("=" * 50)
    logger.info("MARKET ORDER REQUEST")
    logger.info(f"Symbol   : {symbol}")
    logger.info(f"Side     : {side}")
    logger.info(f"Quantity : {quantity}")
    logger.info("=" * 50)

    response = client.place_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_MARKET,
        quantity=quantity,
    )

    logger.info("=" * 50)
    logger.info("MARKET ORDER RESPONSE")
    logger.info(f"Order ID      : {response.get('orderId')}")
    logger.info(f"Status        : {response.get('status')}")
    logger.info(f"Executed Qty  : {response.get('executedQty')}")
    logger.info(f"Average Price : {response.get('avgPrice', 'N/A')}")
    logger.info("=" * 50)

    return response


def place_limit_order(symbol, side, quantity, price):
    """
    Place a LIMIT order.
    """

    logger.info("=" * 50)
    logger.info("LIMIT ORDER REQUEST")
    logger.info(f"Symbol   : {symbol}")
    logger.info(f"Side     : {side}")
    logger.info(f"Quantity : {quantity}")
    logger.info(f"Price    : {price}")
    logger.info("=" * 50)

    response = client.place_order(
        symbol=symbol,
        side=side,
        type=FUTURE_ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce=TIME_IN_FORCE_GTC,
    )

    logger.info("=" * 50)
    logger.info("LIMIT ORDER RESPONSE")
    logger.info(f"Order ID      : {response.get('orderId')}")
    logger.info(f"Status        : {response.get('status')}")
    logger.info(f"Executed Qty  : {response.get('executedQty')}")
    logger.info(f"Average Price : {response.get('avgPrice', 'N/A')}")
    logger.info("=" * 50)

    return response