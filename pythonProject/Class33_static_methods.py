# Static methods in Python are methods that belong to a class rather than an instance of the class. They are defined using the @staticmethod decorator and do not have access to the instance of the class (i.e. self). They are called on the class itself, not on an instance of the class. Static methods are often used to create utility functions that don't need access to instance data.

class Myclass:
    @staticmethod
    def add(a, b):
        print(a+b)

Myclass.add(6,7)  # called without any object