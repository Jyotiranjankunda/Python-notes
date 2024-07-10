# Higher order function - map, filter, reduce

# map(function, iterable)
mylist = [1, 2, 4, 6, 4, 3]
cube = lambda x: x * x * x

newList = list(map(cube, mylist))  # map() will return a map object, so we need to typecase it into list
print(newList)

newList = list(map(lambda x: x * x, mylist))
print(newList)


# filter: The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate (i.e, returns true value)
# filter(function, iterable)

def filter_function(a):
    return a > 3


newList = list(filter(filter_function, mylist))  # Returns a filter object, typecast into list
print(newList)

# reduce: The reduce function is a higher-order function that applies a function to a sequence and returns a single value.
# syntax: reduce(function, iterable)

from functools import reduce

my_sum = reduce(lambda x, y: x + y, mylist)  # Takes 2 values from the list at a time, and add them
print(my_sum)

# It is same as :
'''
my_sum = 0
for i in range(len(mylist)):
    my_sum += mylist[i]
print(my_sum)

'''

