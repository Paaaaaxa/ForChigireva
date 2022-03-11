import numpy as np


def NormaOneForOneLine(Matrix):
    #   вычисляем по максимальной сумме элементов в столбце когда передаётся одномерный массив
    return sum(abs(Matrix))
def NormaInfForOneLine(Matrix):
    return max(abs(max(*Matrix)), abs(min(*Matrix)))
