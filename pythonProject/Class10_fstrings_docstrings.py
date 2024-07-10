# f-strings
name = "Jyotiranjan"
country= "India"

# Before f-strings, we used to print like this
text = "Hey my name is {1} and I am from {0}"
print(text.format(country, name))

# using f-strings
print(f"My name is {name} and I am from {country}")

price = 49.09999
print(f"Price is {price:0.2f} rupees")  # Price is formatted upto 2 decimal places

print(f"2 * 30 = {2*30}")

# If we want to show those curly braces like {name} in console and not the value of name, then we can use double curly braces
print(f"We can use f-strings as follow. My name is {{name}} and I am from {{country}}")

# Docstrings in python
# Python docstrings are the string literals that appear right after the definition of a function, method, class or module.

def square(n):
    '''Takes a number n, and prints its square'''
    print(n ** 2)

square(5)  # Docstring doesn't appear in output. It is only used to tell information about function
print(square.__doc__)  # print docstring like this

'''
Comments vs docstrings

Comments are descriptions that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.
But Python docstrings are strings used right after the definition of a function, method, class, or module. They are used to document our code. We can access these docstrings using the doc attribute.

If any other statement is written before docstring, then it doesn't work, it will print the docstring as None
'''