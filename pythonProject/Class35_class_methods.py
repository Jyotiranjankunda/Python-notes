# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls", which represents the class itself.

# cls is just a naming convention, we can change it anything we want.

# By default it represents an object, but using @classmethod decorator, it represents the class.

# classmethod is used because, we can't change the class variables by any object. Using object, it is only changed for that object only, so for whole class we need @classmethod

class Company:
    company_name = "Google"

    # Since it is a normal function inside the class, so 'self' represents the object that call it
    # def changeCompanyName(self, newName):
    #     self.company_name = newName

    @classmethod
    def changeCompanyName(cls, newName):
        cls.company_name = newName

    def printCompanyName(self):
        print(f"Company name is {Company.company_name}")

c1 = Company()
c1.printCompanyName()

c1.changeCompanyName("Apple")
c1.printCompanyName()
