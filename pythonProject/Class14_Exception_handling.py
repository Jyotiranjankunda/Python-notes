try:
    a = int(input("Enter any no.:"))
    print("Table of", a)
    for i in range(1, 11):
        print(f"{a} * {i} = {a*i}")

    a = [1,2,3,4,5,6]
    print("List:", a)
    ind = int(input("Enter any index of list : "))
    print(a[ind])
except ValueError:
    print("Invalid value")
except IndexError:
    print("Invalid index")
except Exception as e:
    print(e)
    print("Some error occured")
finally:
    print("Finally block always executes irrespective of try or catch")

print("Program finished")

# finally block will be always executed even if it is inside a function, and the function returns a value before finally block
def fun():
    try:
        lst = [1,6,7,8,0]
        i = int(input("enter a no. : "))
        print(lst[i])
        return 1
    except:
        print("Invalid index")
        return 0
    finally:
        print("Always executed")

x = fun()
print(x)

# Raising custom errors
val = int(input("Enter any value between 1 and 10 : "))
if val < 1 or val > 10:
    raise ValueError("Value should be between 1 and 10")
else:
    print("value :", val)

# Defining custom exceptions
'''
In python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

e.g
class CustomError(Exception):
    # code...

try:
    # code...
    
except CustomError:
    # code...
    
    
This is useful because sometimes we might want to do something when a particular exception is raised. For e.g, sending an error report to the admin, calling an api, etc.
'''