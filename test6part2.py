from __future__ import print_function, division

import time
import numpy as np
from numpy import concatenate as cc
import matplotlib.pyplot as plt

w = np.asarray([[0.6, 0.1, 0.1, 0.1, 0.1],
                [0.1, 0.6, 0.1, 0.1, 0.1],
                [0.1, 0.1, 0.6, 0.1, 0.1],
                [0.1, 0.1, 0.1, 0.6, 0.1],
                [0.1, 0.1, 0.1, 0.1, 0.6]])
u = np.transpose(np.asarray([0.6, 0.5, 0.6, 0.2, 0.1]))
m = np.asarray([[-0.125, 0, 0.125, 0.125, 0],
                [0, -0.125, 0, 0.125, 0.125],
                [0.125, 0, -0.125, 0, 0.125],
                [0.125, 0.125, 0, -0.125, 0],
                [0, 0.125, 0.125, 0, -0.125]])

h = np.dot(w, u)

values, vectors = np.linalg.eig(m)

result = 0

for i in range(len(values)):
    value = values[i]
    vector = vectors[:,i]
    dotp = np.dot(h, vector)
    ratio = dotp / (1-value)
    partial = np.dot(ratio, vector)
    result += partial

print(result)
