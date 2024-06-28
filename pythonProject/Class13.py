# Dictionaries : ordered key value pairs.
d = {
    "name": "Jyotiranjan Kunda",
    "age": 23,
    "canVote": True
}

print(d)

# 2 ways to acces any key
print(d["name"])  # This method will throw error if the key is not present
print(d.get("name"))  # It will not throw error if the key is not present, instead it returns None

# print(d.get("xyz"))  ->  None
# print(d["xyz"])  ->  Error

# Access all keys
print(d.keys())

# OR

for key in d.keys():
    print(f"{key}: {d[key]}")

print(d.items())  # It will return a list of key value pairs, and its type is dict_items

for key, val in d.items():
    print(f"{key}: {val}")

# Dictionary methods
emp1 = {
    122: 45,
    123: 89,
    567: 69,
    670: 69
}

emp2 = {
    222: 67,
    566: 90
}

emp1.update(emp2)  # Add add the key value pairs of emp2 into emp1
print(emp1)

# emp2.clear()  # dict will be empty {}
# print(emp2)

# pop : remove any item
emp1.pop(123)
print(emp1)

# popitem : remove the last item
emp1.popitem()
print(emp1)

# del : used to delete the whole dictionary or any item
del emp1[670]
print(emp1)

# del emp2
# print(emp2)  # Whole emp2 dict will be deleted, so this line will give error