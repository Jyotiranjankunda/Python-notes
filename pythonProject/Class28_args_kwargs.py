'''
In Python programming, there are two types of arguments that can be passed in a function.

positional arguments
keyword arguments

Positional arguments are the one in which an order has to be followed while passing arguments like normal functions work with positional arguments.
'''

'''
Keyword arguments:

1. *args:
args is a short form used for arguments. It is used to unpack an argument. In the case of *args, the argument could be a list or tuple. Suppose that we have to enter the name of students who attended a particular lecture. Each day the number of students is different, so positional arguments would not be helpful because we can not leave an argument empty in that case. So the best way to deal with such programs is to define the function using the class name as formal positional argument and student names with parameter *args. In this way, we can pass student's names using a tuple.

Note that the name args does not make any difference, we can use any other name, such as *myargs. The only thing that makes a difference is the Asterisk(*).

2. **kwargs:
The full form of **kwargs is keyword arguments. It passes the data to the argument in the form of a dictionary. Let's take the same example we used in the case of *args. The only difference now is that the student's registration, along with the student's name, has to be entered. So what **kwargs does is, it sends argument in the form of key and value pair. So the student's name and their registration both can be sent as a parameter using a single ** kwargs statement.

Same as we discussed for args*, the name kwargs does not matter. We can write any other name in its place, such as **attendance. The only mandatory thing is the double asterisks we placed before the name.
'''

def funargs(normal_param, *args, **kwargs):
    print(normal_param)

    print("Args :")
    for item in args:
        print(item)

    print("Kwargs :")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

normal = "I am a normal argument"
ls = [45,34,32,23,12]
dct = {
    "Jyotiranjan": "Web Developer",
    "Mukesh": "Analyst",
    "Rajesh": "power bi developer"
}
funargs("I am a normal argument", *ls, **dct)