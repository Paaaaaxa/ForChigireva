def Find(Parent, Child):
    global dClassParent
    #   print(dClassParent)
    if Parent == Child:
        return True
    if Child not in dClassParent or dClassParent[Child] == []:
        return False  # означает, что класс Child вообще не имеет наследников
    if Parent in dClassParent[Child]:
        return True
    else:
        for Element in dClassParent[Child]:
            if Find(Parent, Element):
                return True
    return False


N = int(input())
dClassParent = {}
for i in range(N):
    # заполняем словарь наследования
    lInputList = input().split(" :")
    if len(lInputList) == 1:
        dClassParent[lInputList[0]] = []
    else:
        dClassParent[lInputList[0]] = list(lInputList[1].split())


Count = int(input())
ReadList = []
for i in range(Count):
    ReadList.append(input())
#   ввод
dClassParentNew = {}
for i in range(Count):
    #   проверка на наличие в каждом элементе словаря
    for j in dClassParentNew:
        if Find(j, ReadList[i]):
            print(ReadList[i])
            break
    dClassParentNew[ReadList[i]] = dClassParent[ReadList[i]]

    #
    # if Find(ReadList[i][0], ReadList[i][1]):
    #     print("Yes")
    # else:
    #     print("No")
