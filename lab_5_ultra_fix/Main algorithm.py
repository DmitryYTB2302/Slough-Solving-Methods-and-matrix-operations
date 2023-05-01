import math
import numpy as np
import time
import matplotlib.pyplot as plt

# матрица для проверки работы алгоритма, на загатовленной матрице
checkMatrix = np.array([[1,2,-1],[3,0,2],[4,-2,5]], int)

# формируем рандомную матрицу
def randomFilling(size):
    matrix = np.random.randint(1, 9, (size, size))
    determinant = np.linalg.det(matrix)
    if(determinant != 0):
        return matrix
    else:
        return 0
    return

# алгоритм обращения матриц через присоединенную матрицу
def matrixAttachment(m,size):
    matrix1 = np.transpose(m)
    matrix2 = np.zeros((size,size))
    for i in range (0, size):
        for j in range (0, size):
            alg = np.delete(matrix1, i, axis = 0)
            alg = np.delete(alg, j, axis = 1)
            matrix2[i,j] = ((-1)**(i+j))*np.linalg.det(alg)
    return matrix2 / np.linalg.det(matrix1)

# временные затраты своего алгоритма
def t(size):
    t1 = time.time()
    matrixAttachment(randomFilling(size), size)
    t2 = time.time()
    return t2 - t1

def discrepancy(size):
    T = randomFilling(size)
    b1 = np.linalg.inv(T)
    b2 = matrixAttachment(T,size)
    d = 0
    nev = 0
    d = d + np.sum(b1) - np.sum(b2)
    nev = math.sqrt(d ** 2) / size
    return nev

# график временных затрат совего алгоритма
def chart1():
    a = []
    for i in range(10, 100):
        a.append(t(i))
    fig, ax = plt.subplots()
    plt.xlim(10, 90)
    ax.set_xlabel('Размер системы')
    ax.set_ylabel('Время')
    plt.plot(a, 'red')
    ax.set_title('График времени своего алгоритма от размера системы')
    ax.legend(['Свой алгоритм'])
    plt.grid()
    plt.show()

def chart2():
    a = []
    g = []
    for i in range(1, 90):
        a.append(discrepancy(i))
        g.append(i)
    fig, ax = plt.subplots()
    plt.xlim(10, 100)
    ax.set_xlabel('Размер системы')
    ax.set_ylabel('Время')
    plt.plot(a, 'r')
    plt.yscale('log')
    ax.set_title('График невязки')
    plt.legend(['Свой алгоритм'])
    plt.show()

chart2()