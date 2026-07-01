# Binance Futures Testnet Trading Bot

A Python CLI application to place MARKET and LIMIT orders on the Binance Futures Testnet.

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY and SELL support
- Binance Futures Testnet integration
- Input validation
- Structured logging
- Exception handling
- Modular project structure

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── config.py
│   ├── exceptions.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── .env
├── cli.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <your-github-repo-url>
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=YOUR_TESTNET_API_KEY
BINANCE_SECRET_KEY=YOUR_TESTNET_SECRET_KEY
```

---

## Run

```bash
python cli.py
```

---

## Example

```text
Trading Symbol: BTCUSDT
Side (BUY/SELL): BUY
Order Type (MARKET/LIMIT): MARKET
Quantity: 0.001
```

---

## Logs

API requests, responses, and errors are stored in:

```text
logs/trading.log
```

---

## Tech Stack

- Python 3
- python-binance
- Click
- python-dotenv
- Logging