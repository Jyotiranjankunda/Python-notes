# Set
# sets are unordered collection of data items. not contain duplicate items

s = {2,4,2,6}
print(s)  # 2 is printed once

info = {"Jk", 23, False, 5.9, 19}
print(info, "Type:", type(s))

for item in info:
    print(item)

# dictionary and set both start with curly braces, so we can't create an empty set with {}. It will be treated as dictionary
s = {}
print(type(s))

# empty set
s = set()
print(type(s))

# Set methods
s1 = {1,2,5,6}
s2 = {3,6,7}

# union and update
# union returns a new set where update adds items into the existing set from another set
print(s1.union(s2))
print(s1, s2)  # s1 and s2 are unchanged after union

# s1.update(s2)  # same as union. It changes s1, but union doesn't
# print(s1)

# intersection and intersection_update
# all the update functions change the set, while normal functions don't

print(s1.intersection(s2))
# s1.intersection_update(s2)  #s1 is changed
# print(s1)

# difference and difference_update
print(s1.difference(s2))
# s1.difference_update(s2)
# print(s1)

# symmteric_difference and symmetric_difference_update
# symmetric difference = (s1 union s2) - (s1 intersection s2) or (s1 - s2) union (s2 - s1)

print(s1.symmetric_difference(s2))
# s1.symmetric_difference_update(s2)
# print(s1)

# isdisjoint : no elements in common
print(s1.isdisjoint(s2))

# issuperset
print(s1.issuperset(s2))

# issubset
print(s2.issubset(s1))

# add : add single item
s1.add(56)
s2.add(56)
print(s1, s2)

# update : add more than one item

# remove() / discard()
# The main difference b/w remove and discard is that if we try to delete an item which is not present in the set, then remove() raises an error, while discard doesn't

# s1.remove(5)
# print(s1)

s1.discard(56)
print(s1)

# pop()
# This method removes the last item, but as the set is unordered, so any item can be deleted
popped_item = s1.pop()
print(s1, "Pop:", popped_item)

# del : delete the entire cities
# del s1
# print(s1)  # This will give error, as s1 is deleted

# check if item in set
if 5 in s1:
    print("5 is present")
else:
    print("5 is not present")