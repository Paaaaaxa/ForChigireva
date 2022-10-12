import cmath as cm
import math as m

import numpy as np


def signal(fd, iter): #генерирует сигнал, подаваемый на фильтр.
    point = 0
    Td = 1 / fd
    for k in range(int(iter)):
        # yield (0 * m.sin(2 * m.pi * 100 * point * Td) + 0 * m.sin(2 * m.pi * 500 * point * Td)
        #        + 1 * m.sin(2 * m.pi * 2000 * point * Td))
        if k < 1:
            yield 1
        else:
            yield 0
        point += 1

def SignalAfterFilter(ArrayA_and_B, Fd, points): #возвращает сигнал после прохождения фильтре
    CoefX = ArrayA_and_B[0]
    CoefY = ArrayA_and_B[1]
    OutputSignal = []
    MemoryCellsX = [0] * len(CoefX)
    MemoryCellsY = [0] * len(CoefY)
    for i in signal(Fd, points):
        MemoryCellsX.append(i)
        MemoryCellsX.pop(0)
        MemoryCellsX.reverse()
        MemoryCellsY.reverse()
        OutputSignal.append(sum(np.array(MemoryCellsX) * np.array(CoefX)) +
                            sum(np.array(MemoryCellsY) * np.array(CoefY)))
        MemoryCellsY.reverse()
        MemoryCellsX.reverse()
        MemoryCellsY.append(OutputSignal[-1])
        MemoryCellsY.pop(0)
    return OutputSignal
#   Вычислим коеффициенты для нерекурсивного фильтра
#   и проверим, когда они станут меньше, чем первый в 20 и более раз

fRatio = 0.64  # отношение тау к Т


def DifAndInt(fRatio, flag=str):
    lCoefX = []
    if flag == "d":
        lCoefX.append(1)
        while True:
            lCoefX.append(m.exp((-1 / fRatio) * len(lCoefX)) * (1 - m.exp(1 / fRatio)))
            if abs(lCoefX[1]) > abs(lCoefX[len(lCoefX) - 1] * 20):
                break
        if len(lCoefX) < 10:
            print("Переход к рекурсивной схеме не требуется")
            return lCoefX, [0]
        # для рекурсивного фильтра
        else:
            a0 = 1
            a1 = -1
            b1 = m.exp(-1 / fRatio)
            print("Координата полюса: ", b1 / 1, " Число звеньев в нерекурсивном фильтре: ", len(lCoefX))
            return [a0, a1], [b1]
    if flag == "i":
        lCoefX.append(0)
        while True:
            lCoefX.append(m.exp((-1 / fRatio) * len(lCoefX)) * (m.exp(1 / fRatio) - 1))
            if abs(lCoefX[1]) > abs(lCoefX[len(lCoefX) - 1] * 20):
                break
        if len(lCoefX) < 10:
            print("Переход к рекурсивной схеме не требуется")
            return lCoefX, [0]
        # для рекурсивного фильтра
        else:
            a0 = 0
            a1 = 1 - m.exp(-1 / fRatio)
            b1 = m.exp(-1 / fRatio)
            print("Координата полюса: ", b1 / 1,  " Число звеньев в нерекурсивном фильтре: ", len(lCoefX))
            return [a0, a1], [b1]


#   Расчет звеньев интегрирующей цепи
#   Проведем расчет звеньев цифрового резонатора.

def RezonatorAndRej(Fd, F0, B, flag):
    omega = 2 * m.pi * F0 / Fd
    if flag == "rez":
        alefa = m.pi * B / Fd
        a0 = 1
        b1 = 2 * m.exp(-1 * alefa) * m.cos(omega)
        b2 = -1 * m.exp(-2 * alefa)
        return [a0], [b1, b2]
    if flag == "rej":
        normB = 2 * m.pi * B / Fd
        k1 = -m.cos(omega)
        k2 = (1 - m.sin(normB)) / m.cos(normB)
        return [k1, k2]


def Batter(f0, f1, fd, L):
    T0 = 1 / f0
    T = 1 / fd
    L = pow(10, L / 20)
    # оценим порядок фильтра
    uu = m.log10(2 * L - 1) / (2 * m.log10(f1 / f0))
    N = m.ceil(m.log10(2 * L - 1) / (2 * m.log10(f1 / f0)))
    #    так как имеем ВТОРОЙ порядок фильтра, значит имеем два полюса
    s = []
    for i in range(1, N + 1):
        s.append(cm.exp(-1j * m.pi * (0.5 + (2 * i - 1) / (2 * N))))
    #   произеден расчет полюсов функции,
    #   далее произведем вычисление коэффициентов
    C1 = m.sqrt(2) * T0 / (m.pi * T)
    C2 = pow(T0 / (T * m.pi), 2)
    #   подстановка
    a0 = 1 / (1 + C1 + C2)
    a1 = 2 / (1 + C1 + C2)
    a2 = a0
    b1 = -(2 - 2 * C2) / (1 + C1 + C2)
    b2 = -(1 - C1 + C2) / (1 + C1 + C2)
    return [a0, a1, a2], [b1, b2]
    # return [0.125,0.3745,0.3745,0.125], [0.3333,0.3633,0.0312]

# теперь подадим на фильтры сигналы
# -----------------------------------

# пропустим синтезированный сигнал через фильтр

np.savetxt("OutButter", SignalAfterFilter(Batter(380,760,5000,9), 5000, 300))
np.savetxt("OutDif", SignalAfterFilter(DifAndInt(0.64, "d"), 5000, 300))
np.savetxt("OutItegrator", SignalAfterFilter(DifAndInt(11.4, "i"), 5000, 300))
np.savetxt("OutRez", SignalAfterFilter(RezonatorAndRej(5000,380,20,"rez"), 5000, 300))

RezonatorAndRej(5000, 380,20,"rej")
Batter(380, 760, 5000, 9)
# Coef = DifAndInt(0.84, "d")
Coef2 = DifAndInt(11.4, "i")
# print(Coef, "dif")
print(Coef2, "int")
print(DifAndInt(0.64,"d"), "dif")
print(RezonatorAndRej(5000, 380, 20, "rez"), "rez")

