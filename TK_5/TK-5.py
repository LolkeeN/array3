from math import sqrt


def sqrtFunction(givenList):
    listToReturn = []

    for i in givenList:
        num = sqrt(i)
        listToReturn.append(num)
    return listToReturn