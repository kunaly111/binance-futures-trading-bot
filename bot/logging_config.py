import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("TradingBot")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers
if not logger.handlers:
    file_handler = logging.FileHandler("logs/trading.log")
    file_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)