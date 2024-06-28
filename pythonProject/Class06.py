def findGMean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

findGMean(7,8)  # Calculates the geometric mean of 7 and 8

def isGreater(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

# If we don't want to implement the function right now, and will implement it later, then we can write pass in function body. It will not give any error. The means this current function will be ignored, and next lines of code will be executed.
def fun2():
    pass

x = int(input("Enter first no.: "))
y = int(input("Enter second no.: "))

ans = isGreater(x, y)
match ans:
    case 1:
        print(f"{x} is greater")
    case -1:
        print(f"{y} is greater")
    case _:
        print("Both are equal")

# Default arguments
# Always given at end of the parameters list
def average(x, a=5, b=4):
    print("Average is : ", (x + a + b) / 3)

average(56)  # x = 56, a = 5, b = 4
average(8, 9, 7)  # x = 8, a = 9, b = 7
average(10, 55)  # x = 10, a = 55, b = 4

# variable length arguments
def mean(*numbers):
    sum = 0
    for i in numbers:
        sum += i

    print("Arithmetic mean : ", sum / len(numbers))

mean(1,2,3)  # It will take all these numbers as a tuple

# keyword arbitrary arguments
# While creating a function, pass ** before the parameter name while defining the function. The function access the arguments by processing them in the form of dictionary.
def printName(**name):
    print(type(name))
    print("Hello, my name is", name["fname"], name["lname"])

printName(fname="Jyotiranjan", lname="Kunda")