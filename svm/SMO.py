import random

random.seed(20)

class SMO:
    EPSILON = 10 ** (-3)

    class SMOSolution:
        def __init__(self, n):
            self.alphas = [0.0] * n
            self.b = 0.0


    def calculateE(self, point, points, alphas, b, kernel):
        f = 0.0
        for i in range(len(points)):
            x = points[i]
            value = -1 if x[-1] == 0 else 1
            f += alphas[i] * value * kernel(x[:-1], point[:-1])
        value = -1 if point[-1] == 0 else 1
        return f + b - value

    def solve(self, trainSet, parameters):
        n = len(trainSet)
        c = parameters.c
        tol = parameters.tol
        s = self.SMOSolution(n)
        itersCount = 0
        while itersCount < parameters.eqItersCount:
            numChangedAlphas = 0
            for i in range(n):
                x = trainSet[i]
                valuex = -1 if x[-1] == 0 else 1
                Ei = self.calculateE(x, trainSet, s.alphas, s.b, parameters.kernel[0])
                if (valuex * Ei < -tol and s.alphas[i] < c) or (valuex * Ei > tol and s.alphas[i] > 0.0):
                    j = random.randint(0, n - 1)
                    while j == i:
                        j = random.randint(0, n - 1)
                    y = trainSet[j]
                    Ej = self.calculateE(y, trainSet, s.alphas, s.b, parameters.kernel[0])
                    prevAi = s.alphas[i]
                    prevAj = s.alphas[j]
                    aSum = s.alphas[i] + s.alphas[j]
                    aSub = s.alphas[j] - s.alphas[i]
                    l = h = 0
                    if x[-1] == y[-1]:
                        l, h = max(0.0, aSum - c), min(c, aSum)
                    else:
                        l, h = max(0.0, aSub), min(c, c + aSub)
                    if abs(h - l) <= self.EPSILON:
                        continue
                    val = 2 * parameters.kernel[0](x[:-1], y[:-1]) - parameters.kernel[0](x[:-1], x[:-1]) - parameters.kernel[0](y[:-1], y[:-1])
                    if val >= 0:
                        continue
                    valuey = -1 if y[-1] == 0 else 1
                    s.alphas[j] -= (valuey * (Ei - Ej)) / val
                    if s.alphas[j] > h:
                        s.alphas[j] = h
                    elif s.alphas[j] < l:
                        s.alphas[j] = l
                    if abs(s.alphas[j] - prevAj) < self.EPSILON:
                        continue
                    s.alphas[i] += valuex * valuey * (prevAj - s.alphas[j])
                    b1 = s.b - Ei - valuex * (s.alphas[i] - prevAi) * parameters.kernel[0](x[:-1], x[:-1]) -\
                         valuey * (s.alphas[j] - prevAj) * parameters.kernel[0](x[:-1], y[:-1])
                    b2 = s.b - Ej - valuex * (s.alphas[i] - prevAi) * parameters.kernel[0](x[:-1], y[:-1]) -\
                         valuey * (s.alphas[j] - prevAj) * parameters.kernel[0](y[:-1], y[:-1])
                    if 0 < s.alphas[i] < c:
                        s.b = b1
                    elif 0 < s.alphas[j] < c:
                        s.b = b2
                    else:
                        s.b = (b1 + b2) / 2.0
                    numChangedAlphas += 1
            if numChangedAlphas == 0:
                itersCount += 1
            else:
                itersCount = 0
        return s
