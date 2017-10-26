import os
import os.path
from Message import *

def getData():
    messages = []
    for root, dirs, files in os.walk('.' + os.sep + 'pu1'):
        for file in files:
            foldNum = int(str(root).split('.\pu1\part')[1]) - 1
            isSpam = file.find('spmsg') != -1
            with open(os.path.join(root, file), 'r') as data:
                lines = list(filter(lambda line: len(line.strip()) > 0, data.readlines()))
                lines = [line.rstrip('\n') for line in lines]
                lines = [line.strip() for line in lines]
                subject = (lines[0].lstrip('Subject: ')).split()
                body = lines[1].split()
                messages.append(Message(subject, body, isSpam, foldNum))
    return messages

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
        return 0, tp, tn, fp, fn
    else:
        return 2 * prcision * recall / (prcision + recall), tp, tn, fp, fn
    
def accuracy_score(test, answers):
    accuracy = 0
    size = len(test)
    for i in range(size):
        if test[i] == answers[i]:
            accuracy += 1
    return accuracy / size