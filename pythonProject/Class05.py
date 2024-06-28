# Loops
# For loop
name = "Jyotiranjan"
for i in name:
    print(i)

colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color, ": ")
    for i in color:
        print(i)

# range function
for i in range(11):
    print(i)
    # The range is from 0 to 10

for i in range(1, 101):
    # Range is [1, 101), i.e, 1 to 100
    if(i % 5 == 0):
        print(i)

for i in range(1, 51, 3):
    # The 3rd parameter in range function defines the step, i.e, how many to skip
    # It will print like this: 1, 4, 7, 10 .. etc.
    print(i)

# for loop with else : when loop condition will become false, then control goes to else part
for i in range(5):
    print(i)
else:
    print("loop breaks")

# In this case, else will not execute, bcz it only executes when loop condition becomes false, but here, we are breaking the loop in between

for i in range(5):
    if i == 4:
        break
    print(i)
else:
    print("Loop breaks")


# While loop
i = 0
while i < 10:
    print(i)
    i += 1

# Else with while loop
# When the while loop condition becomes false, the control comes out of the while loop and the else statement is executed
count = -5
while count > 0:
    print(count)
    count -= 1
else:
    print("Count is less than 0")

# There is no do-while loop in python

# Enumerate function in python
# The enumerate function is a built-in function in python that allows you to loop over a sequence (such as list, tuple, string) and get the index and value of each element in the sequence at the same time

fruits = ["mango", "apple", "pineapple", "watermelon", "guava"]
# Here, index, fruit is unpacked as a tuple
for index, fruit in enumerate(fruits):
    print(index, ":", fruit)

# You can also specify a different starting index by passing it as an argiment to the enumerate function
for index, fruit in enumerate(fruits, start=1):
    print(index, ":", fruit)

'''
Difference between :
for i in items:
    for j in items:
        # code ...
        
AND

for i, j in items:
    # code...
'''

'''
1. Nested Loops with `for i in items` and `for j in items`
Here, we have two nested loops, both iterating over the same `items` iterable.

items = [1, 2, 3]

for i in items:
    for j in items:
        print(f"i: {i}, j: {j}")

Output:
i: 1, j: 1
i: 1, j: 2
i: 1, j: 3
i: 2, j: 1
i: 2, j: 2
i: 2, j: 3
i: 3, j: 1
i: 3, j: 2
i: 3, j: 3

2. Single Loop with Unpacking `for i, j in items`
Here, `items` is expected to be an iterable where each element is itself an iterable of two items (like a list of tuples).

items = [(1, 'a'), (2, 'b'), (3, 'c')]

for i, j in items:
    print(f"i: {i}, j: {j}")

Output:
i: 1, j: a
i: 2, j: b
i: 3, j: c
'''
