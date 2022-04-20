import numpy as np
from datetime import datetime

import time
#вводим матрицы А и В
#"{:.8f}"
#print("Введите размерность матрицы")
#N = int(input())
N = 4
# MatrixA = np.zeros((N,N), dtype=float)
# MatrixB = np.zeros((N,1), dtype=float)
#возьму пустую матрицу для x
D = np.zeros((N,N), dtype=float)
B = np.zeros((N,N), dtype=float)
G = np.zeros((N,1), dtype=float)
# print("Введите матрицу А")
# for i in range(N):
#     MatrixA[i] = [float(y) for y in input().split()]
# print("Введите матрицу B")
# for i in range(N):
#     MatrixB[i] = float(input())
# print("Введите матрицу точных решений")
# for i in range(N):
#     XVectorExactly[i] = float(input())

MatrixA = np.array([[-52.4000, 0, -0.5700, 4.7300], [0.1200, 32.4000, 9.0500, 0.4900], [0, 5.8800, -175.000, 2.4300],
                    [-5.0100, 2.4300, 1.8700, -76.2000]], float)
Matrixb = np.array([[-1309.1700], [224.1300], [97.4000], [-7800.6200]], float)

XVectorExactly = np.array([[34], [5], [1], [100]], float)

#  приведение системы к виду, удобному для итераций
#  из вида Ax=b, получим вид x=Bx+g, основа для метода Якоби

# ввод оценки погрешности, ввёденное число указывает точность знака после запятой, т.е порядок точности

print("Введите порядок точности")
epsilon = int(input())
epsilon = 10**(-epsilon)
print("Заданная точность:",epsilon,'\n')

print("Введите число итераций")
I = int(input())

start_time = datetime.now() # Начало работы метода Якоби

def Norma(Matrix: np):
    #   вычисляем по максимальной сумме элементов в столбце (бесконечная норма)
    dMaxSum = 0
    for row in Matrix.transpose():
        if sum(abs(row)) > dMaxSum:
            dMaxSum = sum(abs(row))
    return dMaxSum

def Matrix_B(MatrixA):
    for i in range(N):   # Коэфф матрицы B
        for j in range(N):
            if i == j:
                B[i][j] = 0
            else:
                 B[i][j] = -MatrixA[i][j]/MatrixA[i][i] #всё как по формуле
    return B


print("Матрица B:",'\n',Matrix_B(MatrixA),'\n')
print("Норма матрицы B равна ",Norma(Matrix_B(MatrixA)),'\n') #проверяем условие сходимости

def Jacobi(MatrixA, Matrixb):
    X = np.zeros((N, 1), dtype=float)
    for i in range(N):
        G[i] = Matrixb[i] / MatrixA[i][i]
    for i in range(0, I):
        X = Matrix_B(MatrixA).dot(X)+G
    return X

X= Jacobi(MatrixA, Matrixb)
print("Искомая матрица методом Якоби ",'\n',X,'\n' )

end_time = datetime.now() - start_time # Вычисление времени работы метода Якоби
print("Скорость выполнения метода Якоби: ", end_time)

# Относительная погрешность Х
RxVector = XVectorExactly - X                             # Нашли невязку для вектора Х
XAbsoluteError = Norma(RxVector)                          # Абсолютная погрешность (Можно использоать для нахождения точности)
XRelativeError = XAbsoluteError/Norma(XVectorExactly)     # Относительная погрешность
print("Относительная погрешность метода Якоби: ", XRelativeError,"\n")

DeltaNN = XVectorExactly - X
KriteriyIteraciy = Norma(DeltaNN)
print("ОЦЕНКА ТОЧНОСТИ ",KriteriyIteraciy)
print()
if KriteriyIteraciy < epsilon:
    print ("Выполненно достаточное количество итераций")
else:
    print ("НЕДОСТАТОЧНО ИТЕРАЦИЙ ДЛЯ ЗАДАННОЙ ТОЧНОСТИ")

# ___Метод Зейделя___
print()
print("___Метод Зейделя___")

B_down = np.zeros((N,N), dtype=float)       # Нижняя треугольная матрица
B_up = np.zeros((N,N), dtype=float)       # Верхняя треугольная матрица
XZ = np.ones((N,1), dtype=float)  #возьму пустую матрицу для x

start_time2 = datetime.now()   # Начало работы метода Зейделя


def ZEIDEL(MatrixA, Matrixb):
    X_Z = np.ones((N, 1), dtype=float)
    X_X = np.ones((N, 1), dtype=float)

    for itr in range(0, I):  # Количество итераций
        for i in range(N):
            s1 = sum(B[i][j] * X_Z[j] for j in range(i+1, N))
            s2 = sum(B[i][j] * X_X[j] for j in range(i))
            X_Z[i] = s1 + s2 + G[i]

    return X_Z


print("Норма матрицы B равна ",Norma(Matrix_B(MatrixA)),'\n') #проверяем условие сходимости


X_Z = ZEIDEL(MatrixA, Matrixb)
end_time2 = datetime.now() - start_time2    # Вычисление времени работы метода Зейделя
print("Скорость выполнения метода Зейделя: ", end_time2)
print("Искомая матрица методом Зейделя ", '\n', X_Z, '\n')

# Относительная погрешность Х
Rx_Z_Vector = XVectorExactly - X_Z
XAbsoluteError2 = Norma(Rx_Z_Vector)                        # Абсолютная погрешность (Можно использоать для нахождения точности)
XRelativeError2 = XAbsoluteError2/Norma(XVectorExactly)     # Относительная погрешность
print("Относительная погрешность метода Зейделя: ", XRelativeError2, "\n")

DeltaNN_Z = XVectorExactly - X_Z
KriteriyIteraciy_Z = Norma(DeltaNN_Z)
print("ОЦЕНКА ТОЧНОСТИ ", KriteriyIteraciy_Z)
print()
if KriteriyIteraciy_Z < epsilon:
    print("Выполненно достаточное количество итераций")
else:
    print("НЕДОСТАТОЧНО ИТЕРАЦИЙ ДЛЯ ЗАДАННОЙ ТОЧНОСТИ")


#print("Нижняя треугольная матрица B: \n", B_down)
#print("Верхняя треугольная матрица B: \n", B_up)

#--------------------------------------------------------
# А ТЕПЕРЬ НАДО ЗАЕБЕНИТЬ ГРАФИКИ
print (5)
