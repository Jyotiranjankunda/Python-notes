# Inheritance syntax

# class BaseClass:
    # Body of base class
# class DerivedClass(BaseClass):
    # Body of derived class

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show_details(self):
        print(f"Name of employee with ID {self.id} is {self.name}")


class Programmer(Employee):
    def __init__(self, name, id, language):
        super().__init__(name, id)
        self.language = language

    # In Python, super() is used to call methods from a parent class. It allows you to invoke methods defined in the superclass from the subclass. When using super(), you typically pass the current class and self as arguments, like super().__init__(...), to call the superclass's __init__ method.

    def showLanguage(self):
        print(f"Default language of {self.name} is {self.language}")

e1 = Programmer("Jyotiranjan", 345, "C++")
e1.show_details()
e1.showLanguage()

# Types of inheritance
# 1. Single inheritance
# 2. Multiple inheritance
# 3. Multilevel inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# Single inheritance
class Parent:
    def func1(self):
        print("Parent's function")

class Child(Parent):
    def func2(self):
        print("Child's function")

c1 = Child()
c1.func1()
c1.func2()

# 2. Multiple Inheritance : When a class can be derived from more than one base class this type of inheritance is called multiple inheritance.
class Mother:
    mothername = ""

    def mother(self):
        print("Mother name is :", self.mothername)

class Father:
    fathername = ""

    def father(self):
        print("Father name is :", self.fathername)

class Child(Mother, Father):
    def print_child_name(self):
        print(f"Child's father name is : {self.fathername} and mother's name is : {self.mothername}")

ch = Child()
ch.mothername = "XYZ"
ch.fathername = "ABC"
ch.print_child_name()

# 3. Multilevel inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        super().__init__(grandfathername)

        # Instead of this : super().__init__(grandfathername)
        # We can also write it as:
        # Grandfather.__init__(self, grandfathername)
        # Since, here we are not using class name directly, instead using super keyword, so no need to write self
        # super() method is more preferable in python

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)

    def print_name(self):
        print(f"Grandfather name : {self.grandfathername}")
        print(f"Father name : {self.fathername}")
        print(f"Son name : {self.sonname}")

s1 = Son("Raju", "Rampal", "Lal mani")
s1.print_name()

# Hierarchical inheritance : When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
class Vehicle:
    def fun1(self):
        print("Vehicle function")

class Car(Vehicle):
    def fun2(self):
        print("Car is a vehicle and have 4 wheels")

class Bike(Vehicle):
    def fun3(self):
        print("Bike is a vehicle and have 2 wheels")

car = Car()
car.fun1()
car.fun2()

bike = Bike()
bike.fun1()
bike.fun3()

# Hybrid inheritance : Inheritance consisting of multiple types of inheritance is called hybrid inheritance.
class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


object = Student3()
object.func1()
object.func2()
