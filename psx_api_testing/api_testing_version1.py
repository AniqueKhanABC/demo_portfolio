from psx import stocks, tickers
import datetime

tickers = tickers()

data = stocks("SILK")

print(data)