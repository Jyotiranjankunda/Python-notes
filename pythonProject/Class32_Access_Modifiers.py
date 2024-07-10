'''
Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.

Types :
Public access modifier
Private access modifier
Protected access modifier
'''

# 1. Public access modifier

# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Jyotiranjan", 23)
print(s1.name, s1.age)

# 2. Private access modifier

# We cannot use private members outside of class.
# In Python, there is no strict concept of "private" access modifiers. However, a convention is there to indicate that a variable or method should be considered private by prefixing its name with a double underscore (__).
# Code outside the class can still access these "private" variables and methods, but it is generally understood that they should not be accessed or modified.

class PrivateStudent:
    def __init__(self, name, age):
        self.__name = name  # private variable
        self.__age = age

    def __printName(self):  # private function
        print(self.__name, self.__age)

obj = PrivateStudent("JK", 24)
# print(obj.__name, obj.__age)  # This can't be accessed. It is error
# obj.__printName()  # can't access private function

# You cannot directly call a private method using its name. However, you can access private members and methods using name mangling, which appends _ClassName to the beginning of the variable or method name.

# Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses. Names of class-private and superclass-private attributes are transformed by the addition of a single leading underscore and a double leading underscore respectively.

print(obj._PrivateStudent__name, obj._PrivateStudent__age)
obj._PrivateStudent__printName()

# 3. Protected access modifier
# In OOP, "protected" members are intended to be accessed only by the class and its subclasses, indicated in Python by prefixing the member's name with a single underscore (_), e.g., `_my_method`.

# The single underscore is a naming convention and does not enforce access restrictions; it serves as a hint to developers about the intended access level of the member.

class ProtectedStudent:
    def __init__(self):
        self._name = "Jyoti"

    def _funName(self):      # protected method
        return "CodewithJK"

class Subject(ProtectedStudent):       #inherited class
    pass

obj1 = Subject()
print(obj1._name)
obj1._funName()