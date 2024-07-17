# The time module in Python provides a set of functions to work with time-related operations, such as timekeeping, formatting, and time conversions.

import time
from datetime import datetime


def whileLoop():
    i = 0
    while i < 50000:
        i = i+1

def forLoop():
    for i in range(50000):
        pass

# time.time() : The time.time() function returns the current time as a floating-point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time.

init = time.time()
whileLoop()
t_while = time.time() - init

init = time.time()
forLoop()
t_for = time.time() - init

print("While loop time :", t_while)
print("For loop time :", t_for)

# time.sleep() : The time.sleep() function suspends the execution of the current thread for a specified number of seconds. This function can be used to pause the program for a certain period of time, allowing other parts of the program to run, or to synchronize the execution of multiple threads.

print("Hello how are you")
time.sleep(2)
print("This message is printed after 2 seconds")

# time.strftime() : Stands for string format time. It formats a time value as a string, based on a specified format. This function is particularly useful for formatting dates and times in a human-readable format, such as for display in a GUI, a log file, or a report.

curr_time = datetime.now()
formatted_time = curr_time.strftime("%d-%m-%Y %H:%M:%S")
print(formatted_time)