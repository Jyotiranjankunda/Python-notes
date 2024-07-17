class Person:
    name = "Jyotiranjan Kunda"
    occupation = "Web developer"
    age = 23

    def printInfo(self):
        print(f"My name is {self.name} and I am a {self.occupation}. My age is {self.age}")


# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. It must be provided as the extra parameter inside the method definition.

# create objects of class
p = Person()

print(p.occupation)
p.printInfo()

p.name = "Mukesh"
p.occupation = "ML engineer"
p.age = 25
p.printInfo()


# constructors
# A constructor is a special method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when an object of a class is created.

# A constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values to the data members of that class. It cannot return any value other than None.

# In Python, when you define multiple __init__ methods in a class, the last one defined will override any previous ones.
class Employee:
    def __init__(self, name=None, salary=None):
        if name is None or salary is None:
            print("Default constructor")
            self.name = "Unknown"
            self.salary = 0
        else:
            print("Parameterised constructor")
            self.name = name
            self.salary = salary

    def info(self):
        print(f"{self.name}, {self.salary}")


# jk object will be passed automatically to self parameter in the constructor
jk = Employee("Jyotiranjan", 60000)
jk.info()

ap = Employee("xyz", 20000)
ap.info()

xyz = Employee()
xyz.info()
