# In Python, a lambda function is a small anonymous function without a name. It is defined using the lambda keyword and has the following syntax:
# lambda arguments: expression

# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.

# function for calculating square
# Takes an argument x and returns x*x
square = lambda x : x*x
print(square(4))

cube = lambda  x : x*x*x
print(cube(4))

average = lambda x, y, z : (x+y+z) / 3
print(average(5,9,2))

# we can also pass a function inside another function in python - higher order function
def sum(fx, val):
    return val + fx(val)

fx = lambda x: x**x
print(sum(fx, 3))