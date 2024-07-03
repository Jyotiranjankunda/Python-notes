x = 10  # global variable
print(x)

def fun():
    global x
    x = 5
    y = 7
    print(x)
    print(y)

fun()
print(x)  # The original value of global variable x is changed in the function fun.
# print(y)  # This will give error as y is a local variable

# global x : The global keyword is used to declare that this variable is a global one, and should be accessed from the global scope.