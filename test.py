# import yfinance as yf
# import pandas as pd

# # Define the tickers
# tickers = ['BTC-USD', 'ETH-USD', 'SOL-USD']

# # Download data for the tickers
# data = yf.download(tickers, start='2020-01-01', end='2024-12-31', interval='1d')

# # Align data by date (index), and fill missing values with forward fill (or any other method)
# data = data['Adj Close']  # Use 'Adj Close' to align prices

# # Reset the index (optional, for easier handling)
# data = data.reset_index()

# # Save to Excel
# data.to_excel('crypto_data.xlsx', index=False, engine='openpyxl')

# print("Data downloaded and saved to 'crypto_data.xlsx'")
import pandas as pd
from binance.client import Client
import datetime

# Set up Binance API client (no need for API keys for public data)
client = Client()

# Fetch historical BTC data in 1-hour intervals
symbol = "BTCUSDT"
start_date = "2015-03-01"  # Starting date
end_date = "2024-12-31"  # Ending date
timeframe = Client.KLINE_INTERVAL_1HOUR

def fetch_binance_data(symbol, start_date, end_date, timeframe):
    """Fetches historical data from Binance."""
    klines = client.get_historical_klines(symbol, timeframe, start_date, end_date)
    data = []
    for kline in klines:
        data.append([
            datetime.datetime.fromtimestamp(kline[0] / 1000).strftime('%Y-%m-%d %H:%M:%S'),  # Open time
            float(kline[1]),  # Open
            float(kline[2]),  # High
            float(kline[3]),  # Low
            float(kline[4]),  # Close
            float(kline[5]),  # Volume
            0.0  # Agre column, set to 0 as a placeholder
        ])
    return data

# Fetch data
btc_data = fetch_binance_data(symbol, start_date, end_date, timeframe)

# Convert to DataFrame
columns = ["datetime", "open", "high", "low", "close", "vol", "agre"]
df = pd.DataFrame(btc_data, columns=columns)

# Save to CSV with tab-separated values
output_file = "btc_hourly_data.csv"
df.to_csv(output_file, sep="\t", index=False)

print(f"Data saved to {output_file}")
