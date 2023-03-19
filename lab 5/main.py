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

# временные затраты алгоритма
def t(size):
    t1 = time.time()
    matrixAttachment(randomFilling(size), size)
    t2 = time.time()
    return t2 - t1

# временные затраты встроенного алгоритма
def t2(size):
    t1 = time.time()
    np.linalg.inv(randomFilling(size))
    t2 = time.time()
    return t2 - t1

# невязка
def discrepancy(n):
    T = randomFilling(n)
    b1 = np.linalg.inv(T)
    b2 = matrixAttachment(T,n)
    d = 0
    nev = 0
    d = d + np.sum(b1) - np.sum(b2)
    nev = math.sqrt(d ** 2) / n
    return nev

# график временных затрат алгоритма
def chart1():
    a = []
    for i in range(1, 100):
        a.append(t(i))
    fig, ax = plt.subplots()
    plt.xlim(1, 100)
    plt.plot(a,'red')
    ax.set_title('Временные затраты вычисления матрицы с интервалом (1...100)')
    plt.show()

# график сравнения встроенного метода и своего
def chart2():
    a = []
    a2 = []
    for i in range(10, 100):
        a.append(t(i))
        a2.append(t2(i))
    fig, ax = plt.subplots()
    plt.xlim(10, 90)
    plt.plot(a, 'red')
    plt.plot(a2, 'green')
    ax.set_title('Сравнение своего и встроенного алгоритма')
    ax.legend(['Свой', 'Встроенный'])
    plt.show()

# график невязки
def chart3():
    a = []
    g = []
    for i in range(0, 90):
        g.append(i)
        a.append(discrepancy(i))
    fig, ax = plt.subplots()
    plt.xlim(10, 100)
    plt.plot(g, a, 'r')
    plt.yscale('log')
    ax.set_title('График невязки')
    plt.legend(['Функция присоединенной матрицы'])
    plt.show()

#chart1()
#chart2()
#chart3()

print(matrixAttachment(checkMatrix, len(checkMatrix)))
