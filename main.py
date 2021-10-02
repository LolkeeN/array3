from TK_1.TK_1 import createListFromInputNumbers
from TK_2.TK_2 import cortegeWithMinAndMax
from TK_3.TK_3 import someFunction
from TK_4.TK-4 import multiplyFunction
from TK_4.TK-5 import sqrtFunction

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("**********TASK1***************")
    num = input("Enter number of numbers for TK_1")
    createListFromInputNumbers(num)
    print("**********TASK2***************")
    cortegeWithMinAndMax(list)
    print("**********TASK3***************")
    someFunction(list)
    print("**********TASK4***************")
    multiplyFunction()
    print("**********TASK5***************")
    sqrtFunction(list)

