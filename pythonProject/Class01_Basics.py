print('hello world')
print("hello", "world", "hi", sep='-')  # join using separator
print('my name is jyotiranjan ', end='EOL\n')  # end will be appended to the last of the statement

# Data types
a = 23
print(type(a))

b = 23.12
print(type(b))

c = True
print(type(c))

d = "hajdfl"
print(type(d))

e = None
print(type(e))

# print(123 + "hello")  It will not be concatenated unlike javascript

f = complex(2,3)
print(f, "Type:", type(f))

# List: collection of different data types
l1 = [4,2,7.5,"hello", ["apple", "ball"]]
print(l1, "Type:", type(l1))

# Tuple: similar to list but it is immutable
t1 = (1, 2, 3.5, "hello", True, ("parrot", "sparrow"))
print(t1, "Type:", type(t1))

# Dictionary: map data structure
d1 = {
    "name": "Jyotiranjan",
    "age": 23,
    "canVote": True
}
print(d1, "Type:", type(d1))

# Every data type in python is an object
