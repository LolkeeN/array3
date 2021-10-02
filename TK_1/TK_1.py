def createListFromInputNumbers(count):
    numbers = []
    i = 0
    while i < int(count):
        x = int(input("Enter your number: "))
        numbers.append(x)
        i = i + 1
    return numbers


if __name__ == "__main__":
    x = input("Enter amount of numbers")
    print(createListFromInputNumbers(x))
