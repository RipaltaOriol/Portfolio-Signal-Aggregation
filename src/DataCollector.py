import yfinance

class DataCollector:
    def __init__(self, tickers):
        self.tickers = tickers

    def get_returns(self):
        data = yfinance.download(self.tickers, period = "5y", interval = "1d")
        data = data['Close']
        data = data.pct_change().dropna()
        return data
