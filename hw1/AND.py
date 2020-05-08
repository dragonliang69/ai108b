import gd2 as gd
import numpy as np
import math
from numpy.linalg import norm

A = np.array([[0, 1, 1], 
             [1, 0, 1], 
             [1, 1, 1]])
B = np.array([0.0, 0, 1]).transpose()

def sig(x):
    s = 1 / (1 + np.exp(-x))
    return s

def f(p):
    X = p
    Y = np.dot(A, X)
    return norm(Y - B)

p = np.array([0.0, 0, 0]) 
p = gd.gradientDescendent(f, p)
print("\n============================================================================================================\n")

print("p = {}".format(p))

weights = np.array([p[0], p[1]])
bias = p[2]
w1w2 = np.array([[0, 0],
                 [0, 1],
                 [1, 0],
                 [1, 1]])
ans = np.dot(w1w2, weights) + bias
result = []
for i in ans:
    result.append(1) if i >= 0.5 else result.append(0)
print(result)