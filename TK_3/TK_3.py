from statistics import mean


def someFunction(givenList):
    average = mean(givenList)
    listToReturn = []

    for i in givenList:
        num = i / average
        listToReturn.append(num)
    return listToReturn
