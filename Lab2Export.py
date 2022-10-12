import numpy as np
import FunctionFile as fu

#   введем значения, которые требуются по варианту

lLineA = np.array([0, 1, 1, -1, 2, -1], float)
lLineB = np.array([60, 80, 130, -90, 140, 70], float)
lLineC = np.array([1, 1, -2, 1, 1, 0], float)
lLineD = np.array([6, 7, 13, -8, 15, 9], float)
#поставить, для пункта 3

#lLineD = np.array([6.01, 6.99, 13.01, -8.01, 14.99, 9.01], float)
iN = len(lLineB)#   размерность матрицы

def Progonka(lLineA, lLineB, lLineC, lLineD):#  передаем в функцию строки со значениями
    iN = len(lLineB)#   размерность матрицы
    #   проверим выполнение достаточного условия (диаганальное преобладание)
    for k in range(iN):
        if abs(lLineB[k]) < abs(lLineA[k]) + abs(lLineC[k]):
            print("Error")
            return 1

    #   прогоночные коэффицменты для самой первой итерации
    lGamma = [lLineB[0]]
    lAlfa = [lLineC[0] / lGamma[0] * (-1)]
    lBetta = [lLineD[0] / lGamma[0]]

    # прямая прогонка
    for k in range(1, iN): #    цикл начинается с 1
        lGamma.append(lLineB[k] + lLineA[k] * lAlfa[k - 1])
        if k != iN - 1:  # последняя итерация для n-ого варианта
            lAlfa.append(lLineC[k] / lGamma[k] * (-1))
        lBetta.append((lLineD[k] - lLineA[k] * lBetta[k - 1]) / lGamma[k])

    #   обратная прогонка
    lXVector = [0 for i in range(iN)]
    lXVector[iN-1] = lBetta[iN-1]  # значение последней пераменной (x n-ое)
    for k in reversed(range(iN - 1)):  # Цикл по оставшимся переменным
        lXVector[k] = lBetta[k] + lAlfa[k]*lXVector[k+1]
    return lXVector



print(Progonka(lLineA, lLineB, lLineC, lLineD), '\n')


# найдем норму невязки данного решения
#   для этого восстановим матрицу и подставим полученное решение
FullMatrix = np.zeros((iN,iN), float)
for i in range(iN):#    восстановление матрицы
    FullMatrix[i][i] = lLineB[i]
    if i != iN - 1:
        FullMatrix[i][i+1] = lLineC[i]
        FullMatrix[i+1][i] = lLineA[i+1]

CurrentMatrixB = np.dot(FullMatrix, Progonka(lLineA, lLineB, lLineC, lLineD))
#   определим норму невязки
print("Невязка при методе прогонки по первой норме:", fu.NormaOneForOneLine(CurrentMatrixB - lLineD),'\n')
print("Невязка при методе прогонки по inf норме:", fu.NormaInfForOneLine(CurrentMatrixB - lLineD))
