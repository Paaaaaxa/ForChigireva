import numpy as np


#вводим матрицы А и В


N = int(input())
# MatrixA = np.zeros((N,N), dtype=float)
# MatrixB = np.zeros((N,1), dtype=float)
# for i in range(N):
#     MatrixA[i] = [float(y) for y in input().split()]
# for i in range(N):
#     MatrixB[i] = float(input())

MatrixA = np.array([[8, 2, 5], [3, 4, 7], [9, 7, 4]], float)
MatrixB = np.array([[8], [7], [5]], float)
XVectorExactly = np.array([[0.44], [-0.47], [1.08]], float)


MatrixABasic = MatrixA.copy()
MatrixBBasic = MatrixB.copy()

# начало прямого хода метода Гаусса
for i in range(N):
    iMaxNumber = np.where(MatrixA[i:N, i] == max(MatrixA[i:N, i]))  # находим строку с наибольшим элементом в столбце(как оказалось, это массив)
    # Это большой прикол, но похоже, что это именно ссылка на объект
    MasCopyA = np.copy(MatrixA[iMaxNumber[0] + i]) #копируем нцжную строку для двух массивов А и В
    # это глубокая копия и два независимых массива
    MasCopyB = np.copy(MatrixB[iMaxNumber[0] + i])
    MatrixA[iMaxNumber[0] + i] = MatrixA[i]
    MatrixB[iMaxNumber[0] + i] = MatrixB[i]
    MatrixA[i] = MasCopyA
    MatrixB[i] = MasCopyB
    MatrixA[i], MatrixB[i][0] = MatrixA[i] / MatrixA[i][i], MatrixB[i][0] / MatrixA[i][i] # нормируемся на элемент, стоящий в главной диаганали

    #   фонмируем нули в нижней части матрицы путемвычитания
    for j in range(i + 1, N):
        MatrixB[j][0] = MatrixB[j][0] - MatrixB[i][0] * MatrixA[j][i]
        MatrixA[j][i:N] = MatrixA[j][i:N] - MatrixA[i][i:N] * MatrixA[j][i]  # вычитаем строки срезы можно использовать и так: m = MatrixA[2,0:2]

    print(MatrixA)  # печать на каждом шаге
    print(MatrixB)
# обратный ход

for i in reversed(range(N)):
    # находим значение каждой переменной, начиная с последней, и переносим полученные значения в правую часть
    current = MatrixB[i][0] * MatrixA[0:i, i]  # необходимо использовать так как надо иметь транспонированную
    MatrixB[0:i, 0] = MatrixB[0:i, 0] - current.transpose() # производим вычитание из правой части
    MatrixA[0:i, i] = 0.0 #  формируем нули в верхней части матрицы А
    print(MatrixA)  # печать на каждом шаге
    print(MatrixB)


def Norma(Matrix: np):
    #   вычисляем по максимальной сумме элементов в столбце
    dMaxSum = 0
    for row in Matrix.transpose():
        if sum(abs(row)) > dMaxSum:
            dMaxSum = sum(abs(row))
    return dMaxSum

#Norma(MatrixB)
#теперь вычислим невязку для Х и B
XVectorCurrent = MatrixB.copy()#    вектор текущего решения системы
BVectorCurrent = np.dot(MatrixABasic, XVectorCurrent)

RbVector = MatrixBBasic - BVectorCurrent #  нашли невязку для вектора В
RxVector = XVectorExactly - XVectorCurrent #нашли невязку для вектора Х
# найдем абсолютную погрешность для х и в
XAbsoluteError = Norma(RxVector)#это уже просто числа в формате float
BAbsoluteError = Norma(RbVector)
#   найдем относительные погрешности
XRelativeError = XAbsoluteError/Norma(XVectorExactly)
BRelativeError = BAbsoluteError/Norma(MatrixBBasic)


#Получим оценку числа обусловленности
print("Число обусловленности не менее данной величины")
print(BRelativeError/XRelativeError)





