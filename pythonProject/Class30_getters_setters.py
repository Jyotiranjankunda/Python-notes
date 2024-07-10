# Getters in Python are methods that are used to access the values of an object's properties. They are used to return the value of a specific property, and are typically defined using the @property decorator.

class C:
    def __init__(self, age):
        self._age = age
    # A leading underscore _ is a convention to indicate that an attribute is intended to be private.
    # Even though _age is intended to be private, you can still access it directly from an instance of the class


    # The @property decorator is used to define a method as a property. This allows you to access the method like an attribute, without needing to use parentheses () to call it.
    # When you use @property, it defines a method that acts as a getter.

    @property
    def print_age(self):
        return self._age

    # It is important to note that the getters do not take any parameters and we cannot set the value through getter method.For that we need setter method which can be added by decorating method with @property_name.setter
    @print_age.setter
    def print_age(self, new_value):
        if new_value < 0:
            raise TypeError("Age can't be negative")
        else:
            self._age = new_value


obj = C(23)
print(obj._age)
print(obj.print_age)  # don't call this method as print_age(), bcz by using @property it acts like a value

new_age = int(input("Enter new age : "))
obj.print_age = new_age
print("New age : ", obj.print_age)

