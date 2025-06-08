import numpy as np

class Statistics:
    def __init__(self, rets = None):
        self.rets = rets

    def set_rets(self, rets):
        self.rets = rets

    def get_mu(self, is_vecotr = True):
        if is_vecotr:
            return np.mean(self.rets, axis = 0).to_numpy().reshape(-1, 1)
        self.rets.mean()

    def get_cov(self, bias = False):
        return np.cov(self.rets, bias = bias, rowvar=False)

    @staticmethod
    def get_ones(dims, transpose = False):
        return np.ones((1, dims)) if transpose else np.ones((dims, 1))
