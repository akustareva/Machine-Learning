import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

def getData(file):
    data = pd.read_table(file, sep=",", names=['x', 'y', 'class'])
    return data

def showData(data):
    colorsMap = ['#000000', '#FFFFFF']
    plt.scatter(data['x'].as_matrix(), 
                data['y'].as_matrix(), 
                c=[colorsMap[n] for n in data['class'].as_matrix()])
    plt.show()

def f1_score(test, answers):
    tp = fp = tn = fn = 0
    for i in range(len(test)):
        if test[i] == answers[i] and test[i] == 0:
            tn += 1
        elif test[i] == answers[i] and test[i] == 1:
            tp += 1
        elif test[i] != answers[i] and test[i] == 1:
            fp += 1
        else:
            fn += 1
    recall = tp / (tp + fn) if tp + fn > 0 else 1 if fp == 0 else 0
    prcision = tp / (tp + fp) if tp + fp > 0 else 1 if fn == 0 else 0
    score = 0
    if prcision + recall != 0:
        score = 2 * prcision * recall / (prcision + recall)
    return score, tp, tn, fp, fn

def kFold(dataLen, foldsCount, shuffle=False):
    indexes = np.arange(dataLen)
    if shuffle:
        random.shuffle(indexes)
    fold_sizes = (dataLen // foldsCount) * np.ones(foldsCount, dtype=np.int)
    fold_sizes[:dataLen % foldsCount] += 1
    current = 0
    for fold_size in fold_sizes:
            start, stop = current, current + fold_size
            yield np.concatenate((indexes[0:start], indexes[stop:dataLen])), indexes[start:stop]
            current = stop

def linear_kernel(x1, x2):
    return np.dot(x1, x2)

def gaussian_kernel(x, y, sigma=5.0):
    return np.exp(-np.linalg.norm(x-y)**2 / (2 * (sigma ** 2)))

def polynomial_kernel(x, y, d=3):
    return (1 + np.dot(x, y)) ** d

def rbf_kernel(x, y, gamma=5): # Radial Basis Function
    return np.exp(-gamma * np.linalg.norm(x-y)**2)