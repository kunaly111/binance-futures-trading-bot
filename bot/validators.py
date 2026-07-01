from bot.exceptions import ValidationError


VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol: str):
    if not symbol:
        raise ValidationError("Symbol cannot be empty.")

    return symbol.upper()


def validate_side(side: str):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            f"Invalid side. Choose from: {VALID_SIDES}"
        )

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValidationError(
            f"Invalid order type. Choose from: {VALID_ORDER_TYPES}"
        )

    return order_type


def validate_quantity(quantity):
    try:
        quantity = float(quantity)
    except ValueError:
        raise ValidationError("Quantity must be a number.")

    if quantity <= 0:
        raise ValidationError("Quantity must be greater than 0.")

    return quantity


def validate_price(price, order_type):
    if order_type == "LIMIT":

        if price is None:
            raise ValidationError(
                "Price is required for LIMIT orders."
            )

        try:
            price = float(price)
        except ValueError:
            raise ValidationError("Price must be a number.")

        if price <= 0:
            raise ValidationError(
                "Price must be greater than 0."
            )

        return price

    return None