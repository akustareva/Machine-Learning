import matplotlib.pyplot as plt
import numpy as np

def load_data(filename):
    mndata = np.load(filename, 'rb')
    (_, x_test), (_, x_train), (_, x_valid), (_, y_valid), (_, y_train), (_, y_test) = mndata.items()
    x_train = np.concatenate((x_train, x_valid))
    y_train = np.concatenate((y_train, y_valid))
    
    return x_train, y_train, x_test, y_test

def sigmoid(x):
    return 1./(1 + np.exp(-x))

def sigmoid_deriv(x):
    f = sigmoid(x)
    return np.diag(f * (1 - f))

def softmax(x):
    return np.exp(x) / np.exp(x).sum()

def softmax_deriv(x):
    p = softmax(x)
    return np.diag(p) - np.outer(p, p)
