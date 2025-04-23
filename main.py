import pandas as pd

from src.DataCollector import DataCollector

tickers = pd.read_csv("data/stock_etf_tickers.csv")
print(tickers)
data_collector = DataCollector(tickers)
data_collector.get_returns()
