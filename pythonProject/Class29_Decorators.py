# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

# Decorator is like a middleware or blackbox, which takes a function, perform some operations on it, and return back the modified function

def greet(fx):
    def greetings(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using the function")
    return greetings

@greet
def fun():
    print("Hello world")

fun()
# or it can also be written in function currying format
greet(fun)()

@greet
def add(*args, **kwargs):
    sum = 0

    # isinstance(args[0], list) is used to check whether the first element in the args tuple is of type list
    if len(args) == 1 and isinstance(args[0], list):
        for i in args[0]:
            sum += i
    else:
        for i in args:
            sum += i

    print("Sum is :", sum)

add(6,7,9,2,8)
add([6,7,9,2,8])

# We can also use function currying syntax
greet(add)(9,2,4,5)


# Decorators are often used to add functionality to functions and methods, such as logging, memoization, and access control.
# practical e.g

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_function_call(fx):
    def decorated_fun(a, b):
        logging.info(f"Calling function {fx.__name__} with arguments {a} and {b}")
        result = fx(a, b)
        logging.info(f"{fx.__name__} return {result} as result")
        return result
    return decorated_fun

@log_function_call
def my_fun(a, b):
    return a+b

print(my_fun(9,8))