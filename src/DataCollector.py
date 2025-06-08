import pandas as pd
import yfinance as yf
class DataCollector:
    def __init__(self, tickers, beg, end):
        self.tickers = tickers
        self.beg = beg
        self.end = end

    def get_prices(self):
        data = None
        if self.beg and self.end:
            data = yf.download(self.tickers, start = self.beg, end = self.end, auto_adjust=True)
        else:
            data = yf.download(self.tickers, period = "5y", interval = "1d", auto_adjust=True)
        data = data['Close'] if isinstance(data, pd.DataFrame) else None
        return data

    def get_returns(self):
        data = None
        if self.beg and self.end:
            data = yf.download(self.tickers, start = self.beg, end = self.end, auto_adjust=True)
        else:
            data = yf.download(self.tickers, period = "5y", interval = "1d", auto_adjust=True)
        data = data['Close'] if isinstance(data, pd.DataFrame) else None
        data = data.pct_change().dropna() if isinstance(data, pd.DataFrame) else None
        return data
