import yfinance as yf
import pandas as pd

# Read tickers from a CSV file
df = pd.read_csv('#path to csvfile')
tickers_list = df['Symbol'].tolist()  # Assuming 'A' is the column name

# Threshold for percentage change
threshold = 5

# Fetch the data for these tickers
for ticker_symbol in tickers_list:
    data = yf.Ticker(ticker_symbol)
    hist = data.history(period="2d")

    if len(hist) > 1:
        today = hist.iloc[-1]  # today's data
        yesterday = hist.iloc[-2]  # yesterday's data
        change = ((today['Close'] - yesterday['Close']) / yesterday['Close']) * 100

        if abs(change) >= threshold:
            print(f"The price of {ticker_symbol} has changed by {change}% since yesterday.")

# After checking the list, ask for a specific ticker from the user
ticker_symbol = input("\nPlease enter the ticker symbol: ")

# Fetch the data for this ticker
data = yf.Ticker(ticker_symbol)

# Fetch the historical market data for last 2 days
hist = data.history(period="2d")

# Calculate the percentage change
if len(hist) > 1:
    today = hist.iloc[-1]  # today's data
    yesterday = hist.iloc[-2]  # yesterday's data
    change = ((today['Close'] - yesterday['Close']) / yesterday['Close']) * 100
    print(f"\nThe current price of {ticker_symbol} is {today['Close']}.")
    print(f"It has changed by {change}% since yesterday.")
else:
    print(f"\nNot enough data available for {ticker_symbol}. Try again during market hours.")
