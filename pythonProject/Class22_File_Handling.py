# open the file in read mode 'r'
f = open("files/myfile.txt", 'r')
text = f.read()
print(text)
f.close()

'''
Modes in file
There are various modes in which we can open files.

1. read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
2. write (w): This mode opens the file for writing only and creates a new file if the file does not exist. 
3. append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
4. create (x): This mode creates a file and gives an error if the file already exists.
5. text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
6. binary (b): used to handle binary files (images, pdfs, etc).
'''

# writing file
f = open("files/xyz.txt", 'w')
f.write("Hello world, this is file 2 ")  # It will overwrite the existing text
f.close()

f = open("files/xyz.txt", 'r')
print(f.read())
f.close()

f = open("files/xyz.txt", 'a')
f.write("This is appended text")
f.close()

# 'with' statement : you can use the with statement to automatically close the file after you are done with it.
with open("files/xyz.txt", 'a') as f:
    f.write(" \nFile is written using with block")

# readline() method
# It reads a single line from a file. If we want to read multiple lines, we can use a loop

with open("files/myfile.txt", 'r') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            print("File ends")
            break


# writelines method
# It writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple. Writelines() method does not add newline characters between the strings in the sequence. Do that manually.

lines = ["line1\n", "line2\n", "line3\n"]
with open("files/writeableFile.txt", 'w') as f:
    f.writelines(lines)

# seek() and tell() function
# seek() function : The seek() function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position.

# tell function
# The tell() function returns the current position within the file, in bytes. This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position

with open("files/myfile.txt", 'r') as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(20)  # It will read 20 characters after 10th position in the file
    print(data)
    print(f.tell())

# Truncate function
# When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a', the file is opened in write mode and you can write to the file. However, if you want to truncate the file to a specific size, you can use the truncate function.

with open("files/demo.txt", 'a') as f:
    f.write("Hi friends, i am writing this file ")
    f.truncate(15)  # Only 15 characters will be appended, i.e, Hi friends, i a

