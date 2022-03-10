import numpy as np

#   введем значения
# LineA = np.zeros((1,N), float)
# LineB
lLineA = np.array([0, 1, 1, -1, 2, -1], float)
lLineB = np.array([60, 80, 130, -90, 140, 70], float)
lLineC = np.array([1, 1, -2, 1, 1, 0], float)
lLineD = np.array([6, 7, 13, -8.01, 15, 9], float)


def Progonka(lLineA, lLineB, lLineC, lLineD):
    iN = len(lLineB)
    #   проверим выполнение достаточного условия
    for k in range(iN):
        if abs(lLineB[k]) < abs(lLineA[k]) + abs(lLineC[k]):
            print("Error: Компьютер послал вас нахер!")
            return 1

    #   прогоночные коэффицменты
    lGamma = [lLineB[0]]
    lAlfa = [lLineC[0] / lGamma[0] * (-1)]
    lBetta = [lLineD[0] / lGamma[0]]

    # прямая прогонка
    # сделаем для трех вариантов: k = 1; 2...n-1; n
    # lGamma.append(lLineB[0])
    # lAlfa.append(lLineC[0] / lGamma[0] * (-1))
    # lBetta.append(lLineD[0] / lGamma[0])
    for k in range(1, iN):
        lGamma.append(lLineB[k] + lLineA[k] * lAlfa[k - 1])
        if k != iN - 1:  # последняя итерация для n-ого варианта
            lAlfa.append(lLineC[k] / lGamma[k] * (-1))
        lBetta.append((lLineD[k] - lLineA[k] * lBetta[k - 1]) / lGamma[k])

    #   обратная прогонка
    lXVector = [0 for i in range(iN)]
    lXVector[iN-1] = lBetta[iN-1]  # значение последней пераменной
    for k in reversed(range(iN - 1)):  # Цикл по оставшимся переменным
        lXVector[k] = lBetta[k] + lAlfa[k]*lXVector[k+1]
    return lXVector

print(Progonka(lLineA, lLineB, lLineC, lLineD))
