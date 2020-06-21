import numpy as np


class Functions:
    """Set of mathematical functions."""

    @staticmethod
    def he_initialize(shape):
        he = np.random.normal(loc=0, scale=np.sqrt(1 / shape[0]))
        return he * np.random.randn(*shape)

    @staticmethod
    def set_bias_as_weight(shape):
        return shape[0] + 1, shape[1]

    @staticmethod
    def add_bias(vector):
        return np.hstack([vector, np.ones((vector.shape[0], 1))])

    @staticmethod
    def sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @staticmethod
    def shuffle_vectors(x, y):
        rd = np.arange(len(x))
        np.random.shuffle(rd)
        x = x[rd]
        y = y[rd]
        return x, y

