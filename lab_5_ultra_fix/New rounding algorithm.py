import math
import numpy as np
import time
import matplotlib.pyplot as plt

ar1 = []
ar2 = []
ar3 = []
ar4 = []

n1 = []
n2 = []
n3 = []
n4 = []

size = range(3, 30)

def matrixAttachment(m,size):
    matrix1 = np.transpose(m)
    matrix2 = np.zeros((size,size))
    for i in range (0, size):
        for j in range (0, size):
            alg = np.delete(matrix1, i, axis = 0)
            alg = np.delete(alg, j, axis = 1)
            matrix2[i,j] = ((-1)**(i+j))*np.linalg.det(alg)
    return matrix2 / np.linalg.det(matrix1)

def matrixAttachmentRound(m, size, e):
    matrix1 = np.transpose(m)
    matrix2 = np.zeros((size, size))
    for i in range(0, size):
        for j in range(0, size):
            alg = np.delete(matrix1, i, axis=0)
            alg = np.delete(alg, j, axis=1)
            matrix2[i, j] = np.round(((-1) ** (i + j)) * np.linalg.det(alg), e)
    return np.round(matrix2 / np.linalg.det(matrix1), e)

def discrepancy(m, m2, size):
    identity_matrix = np.identity(size)
    product_matrix = np.dot(m, m2)
    residual_matrix = np.abs(identity_matrix - product_matrix)
    return np.max(residual_matrix)

def chart1():
    for i in size:
        m = np.random.randint(1, 9, size=(i, i))
        # встроенный метод
        t1 = time.time()
        np.linalg.inv(m)
        t2 = time.time() - t1
        ar1.append(t2)
        # метод без округления
        t1 = time.time()
        matrixAttachment(m, len(m))
        t2 = time.time() - t1
        ar2.append(t2)
        # метод с округлением до 3
        t1 = time.time()
        matrixAttachmentRound(m, len(m), 3)
        t2 = time.time() - t1
        ar3.append(t2)
        # метод с округлением до 6
        t1 = time.time()
        matrixAttachmentRound(m, len(m), 6)
        t2 = time.time() - t1
        ar4.append(t2)
    fig, ax = plt.subplots()
    ax.set_title('График сравнения от типа представления')
    ax.set_xlabel('Размерность системы')
    ax.set_ylabel('Время')
    plt.grid()
    plt.plot(size, ar1, '-r')
    plt.plot(size, ar2, '-b')
    plt.plot(size, ar3, '-g')
    plt.plot(size, ar4, '-y')
    plt.legend(['Встроенный', 'Без округления', 'Округление до 3', 'Округление до 6'])
    plt.show()

def chart2():
    for i in size:
        m = np.random.randint(1, 9, size=(i, i))

        inv_m_builtin = np.linalg.inv(m)
        residual_builtin = discrepancy(m, inv_m_builtin, i)
        n1.append(residual_builtin)

        inv_m_no_rounding = matrixAttachment(m, len(m))
        residual_no_rounding = discrepancy(m, inv_m_no_rounding, i)
        n2.append(residual_no_rounding)

        inv_m_round_3 = matrixAttachmentRound(m, len(m), 3)
        residual_round_3 = discrepancy(m, inv_m_round_3, i)
        n3.append(residual_round_3)

        inv_m_round_6 = matrixAttachmentRound(m, len(m), 6)
        residual_round_6 = discrepancy(m, inv_m_round_6, i)
        n4.append(residual_round_6)

    plt.plot(size, n1, label='Встроенный метод')
    plt.plot(size, n2, label='Без округления')
    plt.plot(size, n3, label='Округление до 3')
    plt.plot(size, n4, label='Округление до 6')
    plt.xlabel('Размер матрицы')
    plt.ylabel('Невязка')
    plt.xlim(3, 30)
    plt.title('Сравнение невязок разных методов обращения матриц')
    plt.yscale('log')
    plt.legend()
    plt.grid()
    plt.show()

chart2()


