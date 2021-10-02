from statistics import mean


def multiplyFunction(givenList):
    average = mean(givenList)
    listToReturn = []

    for i in givenList:
        num = i * average
        listToReturn.append(num)
    return listToReturn