import numpy as np

class Layer:
    def __init__(self, shape, activ_func, activ_func_deriv):
        self.ws = np.random.normal(0, 0.02, shape)
        self.b = np.random.normal(0, 0.02, shape[1])
        self.activ_func = activ_func
        self.activ_func_deriv = activ_func_deriv
    
    def forward(self, img):
        self.img = img
        self.input = np.dot(self.img, self.ws) + self.b
        self.result = self.activ_func(self.input)
        return self.result

    def backpropagation(self, delta, learning_rate, moment):
        dB = np.dot(delta, self.activ_func_deriv(self.input))
        dWs = np.outer(self.img, dB)
        delta = np.dot(dB, self.ws.T)
        self.ws -= learning_rate * (dWs + moment * self.ws.mean())
        self.b -= learning_rate * dB
        return delta
