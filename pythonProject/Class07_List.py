# List
l = [3,6,8,9,1,7,34,78,12,33,56,90,11]

# contains or not
# same thing exists in string
if 7 in l:
    print("yes")

print(l)
print(l[:])  # 0 to len(l)
print(l[0:]) # same 0 to len(l)

# jump index
print(l[0::2])  # 3rd parameter is jump index, it will take 2 steps at a time

'''
List comprehension
- Used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

syntax:
list = [Expression(item) for item in Iterable if Condition]

Expression: It is the item which is being iterated.
Iterable: It can be list, tuples, dictionaries, sets and even in arrays or strings
Condition: It checks if the item should be added to the new list or not.
'''

lst = [i for i in range(1, 11)]
print(lst)

lst = [i for i in range(11) if i%2 == 0]
print(lst)

lst = [i*i for i in range(11)]
print(lst)

names = ["ram", "shyam", "ramesh", "gopal", "mukesh"]
print([item for item in names if "h" in item])

# ------------------- List Methods ----------------------
l = [11, 45, 1, 2, 4, 6]

# append
# l.append(7)
# print(l)

# reverse
# l.reverse()
# print(l)

# sort
# l.sort()  # Ascending
# l.sort(reverse=True)  # Descending
# print(l)

print(l.index(4))  # returns the index of first occurence
print(l.count(45))

# l2 = l;  # l2 and l points to the same memory address. Change in one will affect other
l2 = l.copy()  # It will create l2 at a new memory address. Change in one will not affect the other
l2 = [i+1 for i in l2]
print(l)
print(l2)

# l.insert(index, value)
# l.insert(2, 90)
# print(l)

# extend : append elements of one list to another at the end
# l.extend(l2)  # [11, 45, 1, 2, 4, 6, 12, 46, 2, 3, 5, 7]
# print(l)

# another method to concatenate 2 lists
# k = l + l2
# print(k)