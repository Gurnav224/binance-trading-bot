# 🚀 Binance Futures Trading Bot (Testnet)

A CLI-based trading bot built in Python that allows users to place **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)**.

---

## 📌 Features

* ✅ Place **Market Orders**
* ✅ Place **Limit Orders**
* ✅ Supports both **BUY** and **SELL**
* ✅ CLI-based input using `click`
* ✅ Input validation (symbol, side, type, quantity, price)
* ✅ Clean and structured output
* ✅ Logging of requests, responses, and errors
* ✅ Exception handling for invalid inputs and API failures

---

## 🏗️ Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   
|── cli.py             # CLI entry point
├── README.md
├── requirements.txt
├── logs.txt               # Sample logs (Market + Limit)
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot
```

---

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

```
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key
```

> ⚠️ Make sure you use **Binance Futures Testnet API keys**, not production keys.

---

## ▶️ How to Run

### 🔹 Market Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.004
```

---

### 🔹 Limit Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --qty 0.004 --price 30000
```

---

## 🖥️ Example Output

```
📌 Order Request
-------------------------
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.004
Price    : MARKET

📊 Final Order Result
-------------------------
Order ID     : 13001471605
Status       : FILLED
Executed Qty : 0.004
Avg Price    : 66358.80000

✅ Done
```

---

## 📝 Logging

* Logs are stored in: `trading_bot.log`
* Includes:

  * Order requests
  * API responses
  * Errors (if any)

---

## 📄 Sample Logs

Included in `logs.txt`:

* ✅ One Market Order
* ✅ One Limit Order

---

## ⚠️ Assumptions

* Only **USDT trading pairs** are supported (e.g., BTCUSDT)
* Minimum order size follows Binance Futures rules (~$100 notional)
* Limit orders use `GTC` (Good Till Cancelled)
* Testnet environment may return `NEW` before `FILLED`

---

## 🧠 Design Decisions

* **Separation of Concerns**

  * `client.py` → API layer
  * `orders.py` → business logic
  * `validators.py` → validation
  * `cli.py` → user interface

* **Error Handling**

  * Graceful handling of invalid inputs and API errors

* **Logging**

  * Helps debug and trace execution

---

## 🚀 Future Improvements

* Add Stop-Limit / OCO orders
* Add retry mechanism for failed API calls
* Add simple UI (optional)
* Docker support

---

## 👨‍💻 Author

**Gurnav Chaudhary**
Full Stack Developer (MERN)

---

## 📬 Submission

This project was built as part of a coding assignment for a Python Developer Intern role.

---
# binance-trading-bot
