# Input function
# By default, python only take string input, in order to take any other input, we need to typecast it

# a = input("Enter your name : ")
# print(a)
#
# x = int(input("Enter 1st no.: "))
# y = int(input("Enter 2nd no.: "))
# print(x+y)

# Strings in python
# String are immutable

name = '''
Hello,
how are you
what is your name ?
'''
print(name)

# s = "Jyotiranjan"
# for ch in s:
#     print(ch)


# String operations
s1 = "Hello world"
print(len(s1))
print(s1[1:7])  # print from index 1 to 6
print(s1[:4])  # by default takes 1st index as 0, i.e, print from 0 to 3
print(s1[2:])  # print from 2nd index till last

print(s1[0:-3])  # [0, len(s1) - 3]
print(s1[-3:-1])  # [len(s1) - 3, len(s1) - 1]

'''
string:     h  e  l  l  o
+ve index:  0  1  2  3  4
+ve index: -5 -4 -3 -2 -1
'''

print(s1.upper())
print(s1.lower())

s2 = "-----------hello-----------"
print(s2.strip('-'))
# It will remove the trailing - characters from both sides
# lstrip : Remove the trailing - characters from left side
# rstrip : Remove the trailing - characters from right side

print(s1.replace("world", "how are you"))
print(s1.split(' '))  # split by space character, and convert all the splitted strings into a list

blog = "introdUctioN to Python"
print(blog.capitalize())  # output: Introduction to python

print(s1.center(50))  # It will take 50 spaces, the last n spaces are of the string s1, and the remaining 50-n starting spaces are blank
print(s1.count('l'))  # It will count the occurences of 'l' in s1

str1 = "Welcome to python!"
print(str1.endswith('!'))
print(str1.endswith("to", 4, 10))  # Does the string ends with 'to' in the range of [4, 10)
# startsWith -> same as endsWith

str1 = "He is ramesh. He is good boy"
print(str1.find("is"))  # Find the first index of "is", if not found return -1
print(str1.index("is"))  # same as find method, but in case of not found, instead of returning -1, it returns an exception

str1 = "lsdfj34j3j"
print(str1.isalnum())  # alpha numeric can contain 0-9, a-z, and A-Z
print(s1.isalpha())  # checks if the string contains only alphabets, i.e, a-z and A-Z

str1 = "lsjff43543ls"
print(str1.islower())  # checks if the string contains all the lowercase characters, it doesn't care if it contains numbers, or other characters. If string contains uppercase characters, then it returns false

str1 = "lsffn\n"
print(str1.isprintable())  # checks if every character is printable or not, here \n is not printable, hence it returns false

str1 = "Jklsf Lsfj L    Sdlf"
print(str1.isspace())  # returns true if the string contains spaces

print(str1.istitle())  # returns true, if every word of the string is capitalized

# isupper, islower -> checks the case
# swapcase: change every lower case character to upper and vice versa
str1 = "Helo LjPf"
print(str1.swapcase())  # output: hELO lJpF

str1 = "He is ramesh. He is good boy"
print(str1.title())  # converts the string into title case, i.e, first letter of every word is capital