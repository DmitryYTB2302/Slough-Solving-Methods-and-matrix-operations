import math
import time
import numpy as np
import matplotlib.pyplot as plt
from numba import njit

a1 = []
a2 = []
a3 = []
a4 = []

size = range(3, 100)

def randomFilling(size):
    return np.random.randint(1, 9, size=(size, size))

def matrixAttachment(size):
    m = np.random.randint(1, 9, size=(size, size))
    t1 = time.time()
    matrix1 = np.linalg.inv(m)
    t2 = time.time() - t1
    a1.append(t2)
    p1 = time.time()
    matrix1 = np.transpose(m)
    matrix2 = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            alg = np.delete(matrix1, i, axis=0)
            alg = np.delete(alg, j, axis=1)
            matrix2[i, j] = ((-1) ** (i + j)) * np.linalg.det(alg)
    res = matrix2 / np.linalg.det(matrix1)
    p2 = time.time() - p1
    a2.append(p2)
    e = 3
    g1 = time.time()
    matrixTo3 = np.transpose(m)
    matrixTo03 = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            alg1 = np.delete(matrixTo3, i, axis=0)
            alg1 = np.delete(alg1, j, axis=1)
            matrixTo03[i, j] = np.round((((-1) ** (i + j)) * np.linalg.det(alg1)),e)
    res2 = np.round((matrixTo03 / np.linalg.det(matrixTo3)), e)
    g2 = time.time() - g1
    a3.append(g2)
    e = 6
    h1 = time.time()
    matrixTo3 = np.transpose(m)
    matrixTo03 = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            alg1 = np.delete(matrixTo3, i, axis=0)
            alg1 = np.delete(alg1, j, axis=1)
            matrixTo03[i, j] = np.round((((-1) ** (i + j)) * np.linalg.det(alg1)), e)
    res3 = np.round((matrixTo03 / np.linalg.det(matrixTo3)), e)
    h2 = time.time() - h1
    a4.append(h2)

for i in size:
    t2 = time.time()
    p2 = time.time()
    g2 = time.time()
    h2 = time.time()
    matrixAttachment(i)

fig, ax = plt.subplots()
ax.set_xlabel('размерность')
ax.set_ylabel('времязатраты')
plt.plot(size, a1,'g-', label ='Встр. метод')
plt.plot(size, a2,'r-', label ='Алгоритм без округления')
plt.plot(size, a3,'b-', label ='Алгоритм с округлением до 3')
plt.plot(size, a4,'y-', label ='Алгоритм с округлением до 6')
ax.legend()
plt.grid()
plt.show()

