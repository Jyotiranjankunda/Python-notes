# Class variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class

# Instance variable
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class

class Employee:
    no_of_employees = 0
    # This variable is shared among all the objects, and if any object changes the class variable, then it only changes for that object only, not for others

    def __init__(self, name=None):
        self.name = name
        Employee.no_of_employees += 1

    def printNoofEmployees(self):
        print(f"No. of employees in this company : {Employee.no_of_employees}")

obj1 = Employee()
obj2 = Employee("Jyotiranjan")

# Either we call from any of the object, the output will be 2
# The no_of_employees is shared among all instances of the class Employee
obj1.printNoofEmployees()
obj2.printNoofEmployees()

# Note:
# When a function is called using any object, it is actually called like this:
# obj1.printNoofEmployees()  ->  Employee.printNoofEmployees(obj1)
# So, therefore, when we any method is written inside the class, a self parameter is written compulsory to take the reference of object which calls it.
# We can write any name we want, self is not compulsory. But it is mandatory that, the first parameter passed to a function is considered as a reference to the object that calls it.