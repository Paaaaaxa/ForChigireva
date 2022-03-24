def FunctionValue(x):
    return (x - 0.2) ** 3  # вычисляем значение функции


def FunctionDerivative(fX, iMinX, iMaxX, fH):   #    вычисляем производную
    if (fX + fH) > iMaxX:
        return (FunctionValue(fX) - FunctionValue(fX - fH)) / fH
    if (fX - fH) < iMinX:
        return (FunctionValue(fX + fH) - FunctionValue(fX)) / fH
    return (FunctionValue(fX + fH) - FunctionValue(fX - fH)) / (2 * fH)


def NutonMethod(fFirstApproximation, fAccuracy):    #

    fPreviousX = fFirstApproximation
    iNumberOfIteration = 0
    while True:
        fCurrentX = fPreviousX - FunctionValue(fPreviousX) / \
                    FunctionDerivative(fPreviousX, 0, 1, 0.001)

        if (abs(fCurrentX - fPreviousX)) < fAccuracy:
            print(iNumberOfIteration)
            return fCurrentX
        fPreviousX = fCurrentX
        iNumberOfIteration += 1

print(NutonMethod(0.9, 0.0000000001))
