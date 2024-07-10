# The is operator compares the identity of two objects, while the == operator compares the values of the objects. This means that is will only return True if the objects being compared are the exact same object in memory, while == will return True if the objects have the same value.


a = 5
b = 5

print(a == b)  # True
print(a is b)  # True

a = "hello"
b = "hello"

print(a == b)  # True
print(a is b)  # True

a = [1,2,43]
b = [1,2,43]

print(a is b)  # False
print(a == b)  # True

a = (1,2,43)
b = (1,2,43)

print(a is b)  # True
print(a == b)  # True

# In those cases, a and b are both pointing to the same object in memory, so is and == both return True.
# For mutable objects such as lists and dictionaries, is and == can behave differently. 