import math
import pandas as pd
import matplotlib.pyplot as plt

def getData(file):
    data = pd.read_table(file, sep=";", header=0)
    return data

def showData(data):
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    ax.set_xlabel(r'x', fontsize=12)
    ax.set_ylabel(r'y', fontsize=12)
    plt.show()

def showPredictedData(data, predictedData):
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'], label=r"Actual")
    ax.plot(predictedData['x'], predictedData['y'], label=r"Predicted")
    ax.set_xlabel(r'x', fontsize=12)
    ax.set_ylabel(r'y', fontsize=12)
    ax.set_title('Kernel regression')
    ax.legend(loc=2)
    plt.show()

def gaussianKernel(x):
    return 1.0 / math.sqrt(2 * math.pi) * math.exp(-0.5 * x**2)

def epanechnikovKernel(x):
    return (3 / 4) * (1 - x * x)