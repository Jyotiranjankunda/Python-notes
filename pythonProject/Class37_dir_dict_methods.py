# dir, __dict__ and help methods

# dir() : dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.

x = [1, 2, 3]
print(dir(x))  # It will give all the methods and attirbutes related to list x
print(x.__add__)  # Tell what is __add__. whether is a attribute or method
# o/p: <method-wrapper '__add__' of list object at 0x000001B70710D180>

# __dict__ :  The __dict__ attribute returns a dictionary representation of an object's attributes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("XYZ", 56)
print(p.__dict__)

# help() method : The help() function is used to get help documentation for an object, including a description of its attributes and methods.
print(help(Person))