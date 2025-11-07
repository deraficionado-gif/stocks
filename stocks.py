import yfinance as yf
import pandas as pd

# List of tickers
tickers = ["AAPL", "MSFT"]

for symbol in tickers:
    print(f"Downloading data for {symbol}...")
    
    # Download maximum historical data
    df = yf.download(symbol, period="max", auto_adjust=True)
    df.reset_index(inplace=True)
    df = df.round(2)

    # Save CSV in the repo root
    filename = f"{symbol.lower()}_stock.csv"
    df.to_csv(filename, index=False)
    print(f"✅ Saved {filename}")
