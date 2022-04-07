import time as ti
import datetime as dt
import numpy as np
import matplotlib.pyplot as pp

def FunctionValue(x):
    return (x - 0.2) ** 3  # вычисляем значение функции
    #return 2 ** (x - 0.1) - 1
def FunctionValue1(x):
    #return (x - 0.2) ** 3 вычисляем значение функции 1
    return 2 ** (x - 0.1) - 1
def FunctionDerivative(fX, iMinX, iMaxX, fH):  # вычисляем производную 
    if (fX + fH) > iMaxX:
        return (FunctionValue(fX) - FunctionValue(fX - fH)) / fH
    if (fX - fH) < iMinX:
        return (FunctionValue(fX + fH) - FunctionValue(fX)) / fH
    return (FunctionValue(fX + fH) - FunctionValue(fX - fH)) / (2 * fH)

def FunctionDerivative1(fX, iMinX, iMaxX, fH):  # вычисляем производную 1
    if (fX + fH) > iMaxX:
        return (FunctionValue1(fX) - FunctionValue1(fX - fH)) / fH
    if (fX - fH) < iMinX:
        return (FunctionValue1(fX + fH) - FunctionValue1(fX)) / fH
    return (FunctionValue1(fX + fH) - FunctionValue1(fX - fH)) / (2 * fH)

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
print(HalfDelMethod(0, 1, 0.00000001))
#а здесь делаем графики
pp.style.use('seaborn-whitegrid') # стиль графиков
fig = pp.figure() # делаем фигуру
fig1 = pp.figure() # делаем вторую
x = np.arange(0,1,0.001)
y = (x - 0.2) ** 3
y1 = 2 ** (x - 0.1) - 1
y2 = FunctionValue(0.9)+FunctionDerivative(0.9, 0, 1, 0.001)*(x-0.9)#считаем касательные для 1-го графика
x12 = 0.9-((FunctionValue(0.9))/(FunctionDerivative(0.9, 0, 1, 0.001)))#считаем точку пересечения с осью Х
y3 = FunctionValue(x12)+FunctionDerivative(x12, 0, 1, 0.001)*(x-x12)#
x13 = x12-((FunctionValue(x12))/(FunctionDerivative(x12, 0, 1, 0.001)))#
y4 = FunctionValue(x13)+FunctionDerivative(x13, 0, 1, 0.001)*(x-x13)#
y22 = FunctionValue1(0.9)+FunctionDerivative1(0.9, 0, 1, 0.001)*(x-0.9)#считаем теперь для второго
x212 = 0.9-((FunctionValue1(0.9))/(FunctionDerivative1(0.9, 0, 1, 0.001)))#также считаем точку пересечения с осью Х
y23 = FunctionValue1(x212)+FunctionDerivative1(x212, 0, 1, 0.001)*(x-x212)#
x213 = x212-((FunctionValue1(x212))/(FunctionDerivative1(x212, 0, 1, 0.001)))#
y24 = FunctionValue1(x213)+FunctionDerivative1(x213, 0, 1, 0.001)*(x-x213)#
#--------------------------теперь считаем для упрощённого метода Ньютона
ye3 = FunctionValue(x12)+FunctionDerivative(0.9, 0, 1, 0.001)*(x-x12)#
xe13 = x12-((FunctionValue(x12))/(FunctionDerivative(0.9, 0, 1, 0.001)))#
ye4 = FunctionValue(xe13)+FunctionDerivative(0.9, 0, 1, 0.001)*(x-xe13)#
ye23 = FunctionValue1(x212)+FunctionDerivative1(0.9, 0, 1, 0.001)*(x-x212)#теперь для второй функции
xe213 = x212-((FunctionValue1(x212))/(FunctionDerivative1(0.9, 0, 1, 0.001)))#
ye24 = FunctionValue1(xe213)+FunctionDerivative1(0.9, 0, 1, 0.001)*(x-xe213)#
#--------------------------теперь считаем для метода секущих. выбираем для этого первые 2 абсциссы 0.9 и 0.7
ys2 = ((x-0.7)*(FunctionValue(0.9)-FunctionValue(0.7))/(0.9-0.7))+FunctionValue(0.7)
xs12 = 0.7+((FunctionValue(0.7)*(0.7-0.9))/(FunctionValue(0.9)-FunctionValue(0.7)))
ys3 = FunctionValue(xs12)+(((x-xs12)*(FunctionValue(0.7)-FunctionValue(xs12))/(0.7-xs12)))
xs13 = xs12-((0.7-xs12)*FunctionValue(xs12)/(FunctionValue(0.7)-FunctionValue(xs12)))
ys4 = ((x-xs13)*(FunctionValue(xs12)-FunctionValue(xs13))/(xs12-xs13))+FunctionValue(xs13)
ys22 = ((x-0.7)*(FunctionValue1(0.9)-FunctionValue1(0.7))/(0.9-0.7))+FunctionValue1(0.7)#теперь для второй функции
xs212 = 0.7+((FunctionValue1(0.7)*(0.7-0.9))/(FunctionValue1(0.9)-FunctionValue1(0.7)))
ys23 = FunctionValue1(xs212)+(((x-xs212)*(FunctionValue1(0.7)-FunctionValue1(xs212))/(0.7-xs212)))
xs213 = xs212-((0.7-xs212)*FunctionValue1(xs212)/(FunctionValue1(0.7)-FunctionValue1(xs212)))
ys24 = ((x-xs213)*(FunctionValue1(xs212)-FunctionValue1(xs213))/(xs212-xs213))+FunctionValue1(xs213)
ax1 = fig.add_subplot (1,3,1) #делим фигуру на 4 части (первые два числа -  
ax2 = fig.add_subplot (1,3,2) #это на сколько мы делим рядов и столбцов соответственно,
ax3 = fig.add_subplot (1,3,3) #третье число - какую позицию этот график занимает)
ax11 = fig1.add_subplot (1,3,1) #
ax12 = fig1.add_subplot (1,3,2) #
ax13 = fig1.add_subplot (1,3,3) #
ax1.plot(x,y, color='g', linewidth=3)#
ax1.plot(x,y2, color='b', alpha=0.5, label='1-ая итерация')
ax1.plot(x,y3, color='r', alpha=0.5, label='2-ая итерация')
ax1.plot(x,y4, color='y', alpha=1, label='3-я итерация')
ax1.set_title('Метод Ньютона (касательных)', fontsize=15)
ax1.set_xlabel('Ось Х')
ax1.set_ylabel('Ось У')
ax1.legend(loc='best')
ax2.plot(x,y, color='g')#
ax2.plot(x,y2, color='b', alpha=0.5, label='1-ая итерация')
ax2.plot(x,ye3, color='r', alpha=0.5, label='2-ая итерация')
ax2.plot(x,ye4, color='y', alpha=1, label='3-я итерация')
ax2.set_title('Метод Ньютона упрощённый', fontsize=15)
ax2.set_xlabel('Ось Х')
ax2.set_ylabel('Ось У')
ax2.legend(loc='best')
ax3.plot(x,y, color='g')#
ax3.plot(x,ys2, color='b', alpha=0.5, label='1-ая итерация')
ax3.plot(x,ys3, color='r', alpha=0.5, label='2-ая итерация')
ax3.plot(x,ys4, color='y', alpha=1, label='3-я итерация')
ax3.set_title('Метод секущих', fontsize=15)
ax3.set_xlabel('Ось Х')
ax3.set_ylabel('Ось У')
ax3.legend(loc='best')
ax11.plot(x,y1, color='b')#
ax11.plot(x,y22, color='g', alpha=0.5, label='1-ая итерация')
ax11.plot(x,y23, color='r', alpha=0.5, label='2-ая итерация')
ax11.plot(x,y24, color='y', alpha=1, label='3-я итерация')
ax11.set_title('Метод Ньютона (касательных)', fontsize=15)
ax11.set_xlabel('Ось Х')
ax11.set_ylabel('Ось У')
ax11.legend(loc='best')
ax12.plot(x,y1, color='b')#
ax12.plot(x,y22, color='g', alpha=0.5, label='1-ая итерация')
ax12.plot(x,ye23, color='r', alpha=0.5, label='2-ая итерация')
ax12.plot(x,ye24, color='y', alpha=1, label='3-я итерация')
ax12.set_title('Метод Ньютона упрощённый', fontsize=15)
ax12.set_xlabel('Ось Х')
ax12.set_ylabel('Ось У')
ax12.legend(loc='best')
ax13.plot(x,y1, color='b')#
ax13.plot(x,ys22, color='g', alpha=0.5, label='1-ая итерация')
ax13.plot(x,ys23, color='r', alpha=0.5, label='2-ая итерация')
ax13.plot(x,ys24, color='y', alpha=1, label='3-я итерация')
ax13.set_title('Метод секущих', fontsize=15)
ax13.set_xlabel('Ось Х')
ax13.set_ylabel('Ось У')
ax13.legend(loc='best')
pp.show() #Внимание! - Спасибо за внимание!
