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

    def printName(self):
        print("Mother name is :", self.mothername)

class Father:
    fathername = ""

    def printName(self):
        print("Father name is :", self.fathername)

class Child(Mother, Father):
    def print_child_name(self):
        print(f"Child's father name is : {self.fathername} and mother's name is : {self.mothername}")

ch = Child()
ch.mothername = "XYZ"
ch.fathername = "ABC"
ch.print_child_name()

ch.printName()
# This function is common in both Mother and Father classes, so which one will it call. It will call in the order that comes first in inheritance.
# Here, class Child(Mother, Father), so in inheritance, Mother is written first, so printName function of Mother class will be called, not Father.

# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.

print(Child.mro())
# o/p: [<class '__main__.Child'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>]
# First searched in Child, if not found then Mother, then Father, and then Object

# 3. Multilevel inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def print_name(self):
        print(f"Grandfather name : {self.grandfathername}")

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        super().__init__(grandfathername)

        # Instead of this : super().__init__(grandfathername)
        # We can also write it as:
        # Grandfather.__init__(self, grandfathername)
        # Since, here we are not using class name directly, instead using super keyword, so no need to write self
        # super() method is more preferable in python

    def print_name(self):
        super().print_name()
        print(f"Father name : {self.fathername}")

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)

    def print_name(self):
        super().print_name()
        print(f"Son name : {self.sonname}")

s1 = Son("Raju", "Rampal", "Lal mani")
print(s1.mro())

# In this call, print_name function of Grandfather is overriden by Father, and then again by son. First son's print_name function will be called, then it will call Father's print_name func., then it will call Grandfather's print_name function. After Grandfather's func executed, then control goes back to father's function, after than son's func.

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
