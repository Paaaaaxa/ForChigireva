import time as ti
import datetime as dt


def FunctionValue(x):
    return (x - 0.2) ** 3  # вычисляем значение функции
    #return 2 ** (x - 0.1) - 1

def FunctionDerivative(fX, iMinX, iMaxX, fH):  # вычисляем производную
    if (fX + fH) > iMaxX:
        return (FunctionValue(fX) - FunctionValue(fX - fH)) / fH
    if (fX - fH) < iMinX:
        return (FunctionValue(fX + fH) - FunctionValue(fX)) / fH
    return (FunctionValue(fX + fH) - FunctionValue(fX - fH)) / (2 * fH)


def NutonMethod(fFirstApproximation, fAccuracy, sType):  #

    fPreviousX = fFirstApproximation
    fPreviousPreviousX = 0.3  # fFirstApproximation + fAccuracy
    iCountOfIteration = 0
    time_start = ti.time()
    while True:
        if sType == "Метод Ньютона":
            fCurrentX = fPreviousX - FunctionValue(fPreviousX) / \
                        FunctionDerivative(fPreviousX, 0, 1, 0.001)
        if sType == "Метод Ньютона упрощенный":
            fCurrentX = fPreviousX - FunctionValue(fPreviousX) / \
                        FunctionDerivative(fFirstApproximation, 0, 1, 0.001)
        if sType == "Метод секущих":
            fCurrentX = fPreviousX - ((fPreviousX - fPreviousPreviousX)*FunctionValue(fPreviousX) / \
                                      (FunctionValue(fPreviousX) - FunctionValue(fPreviousPreviousX)))
        if (abs(fCurrentX - fPreviousX)) < fAccuracy:
            print("Число итераций метода: ", iCountOfIteration)
            print("Затрачено времени: ", ti.time() - time_start)
            return fCurrentX
        fPreviousPreviousX = fPreviousX
        fPreviousX = fCurrentX
        iCountOfIteration += 1


print("Решение методом Ньютона")
print(NutonMethod(0.9, 0.00000001, "Метод Ньютона"), "\n")

print("Решение упрощенным методом Ньютона")
print(NutonMethod(0.9, 0.00000001, "Метод Ньютона упрощенный"), "\n")

print("Решение методом секущих")
print(NutonMethod(0.9, 0.00000001, "Метод секущих"), "\n")


def HalfDelMethod(fLeftBorder, fRightBorder, fAccuracy):
    if FunctionValue(fLeftBorder) * FunctionValue(fRightBorder) >= 0:
        return "Нет решения на данном интервале"
    iCountOfIteration = 0
    time_start = ti.time()
    while True:
        iCountOfIteration += 1
        fDelta = (fRightBorder - fLeftBorder) / 2
        if fDelta < fAccuracy:
            print("Число итераций метода: ", iCountOfIteration)
            print("Затрачено времени: ", ti.time() - time_start)
            return (fRightBorder + fLeftBorder) / 2
        if FunctionValue(fRightBorder - fDelta) * FunctionValue(fRightBorder) < 0:
            #   тогда корень находится в данном промежутке /( RightBorder - fDelta...fRightBorder) .
            fLeftBorder = fRightBorder - fDelta
        else:
            fRightBorder = fRightBorder - fDelta


print("Решение методом половинного деления")
print(HalfDelMethod(0, 1, 0.000001))
