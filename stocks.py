import yfinance as yf
import os

# -----------------------------
# USER CONFIGURATION
# -----------------------------
symbols = ["AAPL", "MSFT"]  # Apple and Microsoft
folder = "data"             # Folder to save CSVs

# Ensure the folder exists
os.makedirs(folder, exist_ok=True)

# -----------------------------
# DOWNLOAD AND SAVE STOCK DATA
# -----------------------------
for symbol in symbols:
    print(f"Downloading data for {symbol}...")
    df = yf.download(symbol, period="max", auto_adjust=True)
    df.reset_index(inplace=True)
    csv_file = os.path.join(folder, f"{symbol.lower()}_stock.csv")
    df.to_csv(csv_file, index=False)
    print(f"✅ Saved {csv_file}")