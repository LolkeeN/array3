from TK_1.TK_1 import createListFromInputNumbers
from TK_2.TK_2 import cortegeWithMinAndMax
from TK_3.TK_3 import someFunction
from TK_4.TK_4 import multiplyFunction
import importlib

if __name__ == '__main__':
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("**********TASK1***************")
    num = input("Enter number of numbers for TK_1")
    print(createListFromInputNumbers(num))
    print("**********TASK2***************")
    print(cortegeWithMinAndMax(list))
    print("**********TASK3***************")
    print(someFunction(list))
    print("**********TASK4***************")
    print(multiplyFunction(list))
    print("**********TASK5***************")
    tk5 = importlib.import_module("TK_5.TK-5")
    print(tk5.sqrtFunction(list))

