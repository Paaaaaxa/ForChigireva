from MetodProgonki import Progonka
import numpy as np
def FunctionValue(x):
    # return pow(2,x)
    return 1/(1+25*x*x)
Function = []
def FunctionValuePolinom(A, B, C, D, h):
    global Function
    i = 0
    #@asdfv
    grid = h / 10
    while i*grid < h:
        Function.append(A + B*(i*grid) + C*(i*grid)*(i*grid) + D*(i*grid)*(i*grid)*(i*grid))
        i +=1

def RightPart(xMin, xMax, h):
    i = 1
    # начинаем со второго значения функции
    while xMin+(i * h) < xMax:
        x = xMin+(i * h)
        yield 3*((FunctionValue(x + h)-FunctionValue(x))/h -
                 (FunctionValue(x)-FunctionValue(x - h))/h)
        i += 1

def CubSpline(xMin, xMax, h):
    #   формируем вектор правых частей
    #   начинаем с индекса 2
    global Function
    VectorF = [float(i) for i in RightPart(xMin,xMax, h) ]
    VectorA = []
    VectorB = []
    VectorD = []
    CoefA = [0] + [h]*(len(VectorF)-1)
    CoefB = [h]*(len(VectorF)-1) + [0]
    CoefC = [4*h]*len(VectorF)
    VectorC = [0] + Progonka(CoefA,CoefC,CoefB,VectorF)
    for i in range (len(VectorC)):
        if i < len(VectorC) - 1:
            # заполняем вектор коэффициентов С
            VectorB.append(((FunctionValue(xMin + (i+1)*h) - FunctionValue(xMin + i*h))/h) -
                           (1/3)*h*(VectorC[i+1]+2*VectorC[i]))
            # заполняем вектор коэффициентов D
            VectorD.append((VectorC[i+1] - VectorC[i])/(3*h))
        else:
            # заполняем вектор коэффициентов С
            VectorB.append(((FunctionValue(xMin + (i + 1) * h) - FunctionValue(xMin + i * h)) / h) -
                           (2 / 3) * h * VectorC[i])
            # заполняем вектор коэффициентов D
            VectorD.append((0 - VectorC[i])/(3*h))
        VectorA.append(FunctionValue(xMin + (i*h)))
    for i in range(len(VectorC)):
        FunctionValuePolinom(VectorA[i],VectorB[i],VectorC[i],VectorD[i],h)
    p=5

    # print(VectorC)
    # print(VectorD)
    # print(VectorA)
    # print(VectorB)

CubSpline(1, 2, 0.1)

o =7
h = np.array(Function, dtype=float)
np.savetxt("FunctionOut", h)

