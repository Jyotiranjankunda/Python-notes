# Tuple
tup = (1,5)
print(type(tup), tup)

# If we create tuple of only one length, then python treats it as a single variable not tuple, so we need to add a comma at the end to make it tuple
t = (4,)
print(type(t), t)

# Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are immutable.

tp = (1,2,76,342,32,"green", True)
# tp[0] = 5  # We can't change anything in tuple

print(tp, "Length:", len(tp))
print(tp[0])
print(tp[3])
print(tp[-2])

if 342 in tp:
    print("342 is present in tuple")

tp2 = tp[1:5]  # 2, 76, 342, 32

# Methods on tuples
# Tuples are immutable, hence if you want to manipulate tuple, then first convert it into list, perform operation on list, and then again convert it to tuple. Once converting tuple to list, we can perform all list operations on tuple

countries = ("India", "Spain", "Italy", "England", "Germany")
temp = list(countries)
temp.pop()
countries = tuple(temp)
print(countries)

# concatenate 2 tuples
concat_tup = tp + tp2
print(concat_tup)

tuple1 = (0,1,3,2,3,2,3,1,3,2)
print(len(tuple1))
print(tuple1.count((3)))
print(tuple1.index(3))  # First index of 3
print(tuple1.index(3, 4, 8))  # First occurence of index 3 in range 4 to 7, i.e, [4, 8). If not found, then error occurs
