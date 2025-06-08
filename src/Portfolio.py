import numpy as np
from src.Statistics import Statistics
class Portfolio:
    def __init__(self, mu, cov):
        """
        Construct a new "Portfolio" object.

        :param mu: vector of returns
        :param cov: covariance matrix
        """
        self.mu = mu
        self.cov = cov

        self.n = mu.shape[0]
        self.ones = Statistics.get_ones(self.n)
        self.onesT = Statistics.get_ones(self.n, True)
        self.cov_inv = np.linalg.inv(cov)

    def get_MVP_constrained(self, target):
        muT = self.mu.reshape(1, -1)
        A = self.onesT @ self.cov_inv @ self.ones
        B = muT @ self.cov_inv @ self.ones
        C = muT @ self.cov_inv @ self.mu
        delta = A * C - B ** 2
        lambda1 = (C - B * target) / delta
        lambda2 = (A * target - B) / delta
        return lambda1 * self.cov_inv @ self.ones + lambda2 * self.cov_inv @ self.mu

    def get_MVP_unconstrained(self):

        numerator = self.cov_inv @ self.ones
        denominator = self.onesT @ self.cov_inv @ self.ones
        return numerator / denominator

    def get_MVP(self, is_constrained = False, target_mu = None):
        if is_constrained and target_mu is None:
            raise Exception("Constrained MVP needs target return")

        if is_constrained:
            return self.get_MVP_constrained(target_mu)

        return self.get_MVP_unconstrained()

    @staticmethod
    def get_return():
        pass

    @staticmethod
    def get_var():
        pass
