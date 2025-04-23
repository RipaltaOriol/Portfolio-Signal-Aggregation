import numpy as np
from scipy.optimize import minimize

class Portfolio:
    def __init__(self, returns):
        self.returns = returns

        self.mu = returns.mean() * 252
        self.cov = returns.cov() * 252 # double check this

    def get_max_sharpe(self, rf = 0.02):
        n = len(self.mu)

        def portfolio(weights):
            ret = np.dot(weights, self.mu)
            vol = np.sqrt(np.dow(weights.T, np.dow(self.cov, weights)))
            sharpe = (ret - rf) / vol
            return -sharpe

        constraints = {{"type": "eq", "fun": lambda x: np.sum(x) - 1}}
        bounds = tuple((0, 1) for _ in range(n)) # problem here: allow shorts
        init_guess = np.array([1. / n] * n)
        result = minimize(portfolio, init_guess, method = "SLSQP", bounds = bounds, constraints = constraints)

        return result.x
