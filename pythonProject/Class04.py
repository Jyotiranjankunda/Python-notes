applePrice = 160
budget = 200

if(budget - applePrice > 50):
    print("Add 1kg apples")
elif (budget - applePrice > 30):
    print("Ok, you can buy")
else:
    print("Don't buy")

# e.g
import time
t = time.strftime("%H:%M:%S")  # strftime means string format time
print(t)  # It returns a string of current time

hours = int(time.strftime("%H"))
if(hours >= 0 and hours < 12):
    print("Good morning")
elif(hours >= 12 and hours < 17):
    print("Good afternoon")
else:
    print("Good night")

# Short hand if else
# syntax : statement condition
a = 2
b = 300
print("A") if a > b else print("B")
'''
It is similar to:
if a > b:
    print("A")
else:
    print("B")
'''

# e.g
a = 10
b = 10
print("A") if a > b else print("B") if b > a else print("Equal")
'''
It is similar to:
if a > b:
    print("A")
elif b > a:
    print("B")
else:
    print("Equal")
'''

# e.g
# result = value_if_true if condition else value_if_false
c = 9 if a >= b else ""
print(c)

# Match case statements - similar to switch
# Simple match statement
n = int(input("Enter any no. b/w 1 and 3 : "))
match n:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Not between 1 and 3")

# Match case with or operator
num = int(input("Enter a no. b/w 1 and 6 : "))
match num:
    case 1|2:
        print("One or two")
    case 3|4:
        print("Three or four")
    case 5|6:
        print("Five or six")
    case _:
        print("Not between 1 and 6")

# Match case with if statement
inp = int(input("Enter any no. : "))
match inp:
    case num if num > 0:
        print("Positive number")
    case num if num < 0:
        print("Negative number")
    case _ if num == 0:
        print("Zero")

# Match case with sequence patter
def fun(mystr):
    match mystr:
        case ["a"]:
            print("a")
        case ["a", *b]:
            print(f"a and {b}")
        case [*a, "e"] | (*a, "e"):
            print(f"{a} and e")
        case _:
            print("No data")

fun([])
fun(["a"])
fun(["a", "bsdf", 24])
fun((34, 56, True, "hello", "e"))
fun(["b", "c", "d", "e"])

'''
Explanation:

1. case ["a"]
- This pattern matches when mystr is a list containing a single element "a".
- If mystr is ["a"], it prints "a".

2. case ["a", *b]
- This pattern matches when mystr is a list where the first element is "a" and there can be zero or more elements following it.
- If mystr is ["a", "b"], ["a", "c", "d"], etc., it prints "a and {b}", where {b} is the list of the remaining elements.
- The *b syntax means that all elements after "a" will be collected into the list b.

3. case [*a, "e"] | (*a, "e")
- This pattern matches when mystr is a list where the last element is "e" and there can be zero or more elements before it. It also matches tuples with the same condition.
- If mystr is ["b", "c", "d", "e"], ["e"], or ("b", "c", "e"), it prints "{a} and e", where {a} is the list or tuple of all elements before "e".
- The [*a, "e"] syntax collects all elements before "e" into the list a.
'''