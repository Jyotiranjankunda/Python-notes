# A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary.

# For example, consider a class named "Person" that has two attributes: "name" and "age". The default constructor will be:

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# But if we want to create an object whose data is given in form of string separated by comma or some other character, then is should be defined like this :
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def obj_from_string(cls, string):
        name, age = string.split(',')  # destructuring
        return cls(name, int(age))  # This will pass in the constructor, and a new object will be created

    def printPerson(self):
        print(f"Name: {self.name}, Age: {self.age}")

p1 = Person.obj_from_string("Jyotiranjan, 23")
p1.printPerson()


# Another example
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @classmethod
    def square(cls, dimension):
        return cls(dimension, dimension)

    def print_square(self):
        print(f"Square is : {self.height * self.width}")

sqr = Rectangle.square(10)
sqr.print_square()