import yfinance as yf
import os

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# List of stock symbols
stocks = ["AAPL", "MSFT"]

for symbol in stocks:
    print(f"Downloading data for {symbol}...")
    df = yf.download(symbol, period="max", auto_adjust=True)
    df.reset_index(inplace=True)

    # Save CSV in data folder
    filename = f"data/{symbol.lower()}_stock.csv"
    df.to_csv(filename, index=False, float_format="%.2f")
    print(f"✅ Saved {filename}")