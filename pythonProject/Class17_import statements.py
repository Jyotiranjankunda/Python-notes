# How importing in python works

# Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

import math
result = math.sqrt(9)
print(result)

# from keyword : You can also import specific functions or variables from a module using the from keyword.

from math import sqrt, pi
result = sqrt(9)
print(result)
print(pi)

# importing everything : using the * wildcard

from math import *
result = sqrt(9)
print(result)  # Output: 3.0
print(pi)  # Output: 3.141592653589793\

# "as" keyword : Rename imported modules using the as keyword.
import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793

# dir function : Used to view the names of all the functions and variables defined in a module.
import math
print(dir(math))