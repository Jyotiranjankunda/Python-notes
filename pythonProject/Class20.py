# os Module in Python

# The os module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

import os

# Open the file in read-only mode
f = os.open("files/myfile.txt", os.O_RDONLY)

# Read the contents of the file
contents = os.read(f, 1024)
print(contents.decode())  # Decode and print contents

# Close the file
os.close(f)

# To open a file for writing, you can use the os.O_WRONLY flag:

# Open the file in write-only mode
f = os.open("files/myfile.txt", os.O_WRONLY)

# Write to the file
os.write(f, b"Hello, world!")

# Close the file
os.close(f)

# Interacting with the file system
# The os module also provides functions for interacting with the file system. For example, you can use the os.listdir function to get a list of the files in a directory:

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']

# You can also use the os.mkdir function to create a new directory:
# os.mkdir("newdir")

# Running system commands
# Finally, the os module provides functions for running system commands. For example, you can use the os.system function to run a command and get the output:

# Run the "dir" command and print the output
output = os.system("dir")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# You can also use the os.popen function to run a command and get the output as a file-like object:

# Run the "dir" command and get the output as a file-like object
f = os.popen("dir")

# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Close the file-like object
f.close()

# Suppose i want to create n no. of folders, doing it manually is a heavy task. We can do it easily using os module
if(not os.path.exists("newdir")):
    os.mkdir("newdir")

# It wil create folders from Folder 1 to Folder 50
for i in range(50):
    os.mkdir(f"newdir/Folder {i+1}")

folders = os.listdir("newdir")
print(os.getcwd())  # It will get the current working directory

if(os.path.exists("files")):
    os.chdir("files")  # Change the current working directory to files
    print(os.getcwd())
else:
    print("Files directory doesn't exist")

os.chdir("..")
print(os.getcwd())

# if(os.path.exists("pythonProject")):
#     os.chdir("pythonProject")  # Change the current working directory to files
#     print(os.getcwd())
# else:
#     print("pythonProject directory doesn't exist")

for folder in folders:
    print(folder)
    print(os.listdir(f"newdir/{folder}"))  # Print the data of all the folders of newdir folder
