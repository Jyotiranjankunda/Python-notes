# Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties their behaviour.

# Generally used for operator overloading

# __init__ method
# The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object’s initial state, and it is where you would typically define any instance variables that you need. Also called "constructor", we have discussed this method already

# __str__ and __repr__ methods
# The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

# __len__ method
# The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.

# __call__ method
# The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.

# These are just a few of the many magic methods available in Python. They are incredibly powerful tools that allow you to customize the behaviour of your objects, and can make your code much cleaner and easier to understand.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name} and salary: {self.salary}"

    def __repr__(self):
        # repr -> representation
        return f"Employee('{self.name}')"

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        print(f"Employee name: {self.name}, and salary : {self.salary}")


e = Employee("Jyotiranjan", "100000")
print(e)  # It is same as writing : e.__str__()
print(str(e))  # It is same as writing : e.__str__()
print(repr(e))  # It is same as writing : e.__repr__()
print(len(e))  # It is same as writing : e.__len__()
e()  # It is same as writing : e.__call__()

# When we call a function fun(), and it is defined as def fun():
# Then internally it is called like this : fun.__call()__