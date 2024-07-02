# if "__name__ == "__main__"

# It is used to determine whether the script is being run directly or being imported as a module into another script.

# In Python, the __name__ variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the __name__ variable is set to the string __main__ When the script is imported as a module into another script, the __name__ variable is set to the name of the module.

# It is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.

def myfun():
    print("Hello how are you, myfunction is running")


if __name__ == "__main__":
    myfun()

# If name == main not used here, then whenever any other file imports this function and call it, then it will run twice, one by that file, and once here, so to avoid this problem, name == main is used.
