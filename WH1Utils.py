import numpy as np
import matplotlib.pyplot as plt
import random

from mpl_toolkits.mplot3d import Axes3D

def accuracy_score(test, answers):
    accuracy = 0
    size = len(test)
    for i in range(size):
        if test[i] == answers[i]:
            accuracy += 1
    return accuracy / size

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
    if prcision + recall == 0:
        return 0
    else:
        return 2 * prcision * recall / (prcision + recall)

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

def showTrainingResult(test, answers):
    colorsMap = ['#000000', '#FFFFFF', '#FF0000']
    colors = []
    for i in range(len(test)):
        if test[i][1] == answers[i][1]:
            colors.append(colorsMap[test[i][1]])
        else:
            colors.append(colorsMap[2])
    points = np.asarray([point[0] for point in test])
    if points.shape[1] == 2:
        plt.scatter(points[:, 0],
                    points[:, 1],
                    c=colors)
        plt.show()
    else:
        ax = Axes3D(plt.figure())
        ax.scatter(points[:, 0],
                   points[:, 1],
                   points[:, 2],
                   c=colors)
        plt.show()