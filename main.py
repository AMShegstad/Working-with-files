"""
This week we will create a program that performs file processing activities.
Your program this week will use the OS library in order to validate that a directory exists before creating a file in that directory.
Your program will prompt the user for the directory they would like to save the file in as well as the name of the file.
The program should then prompt the user for their name, address, and phone number.
Your program will write this data to a comma separated line in a file and store the file in the directory specified by the user.
Once the data has been written, your program should read the file you just wrote to the file system and
display the file contents to the user for validation purposes.
"""
"""
import os
os.path.isfile('/file.txt') # will return true if the file exists
os.path.isdir('dir') # will return if the true directory exists
os.path.exists('file.txt') # will return true is the file or directory passed to the function exists
"""
import os

"""
def getCompletePath(filePath, fileName):
    completePath = filePath + fileName
    return completePath

def saveUserInfo(completePath, name, address, digits):
    if os.path.exists(completePath):
        print("the path exists")
    print(f"Saving to {completePath}")
    print(completePath)

    with open(completePath, 'w') as file_object:
        file_object.write(f"{name}, {address}, {digits}")

    return completePath, name, address, digits

def readFile(completePath):
    if os.path.exists(completePath):
        print("The path exists")
    with open(completePath, 'r') as file_object:
        contents = file_object.read()
        print(contents)

"""
filePath = input("Please enter the directory to which you'd like to save your file (must end with a '/')\n")
if os.path.isdir(filePath):
    print("The directory exists")
print(filePath)

fileName = 'userData.txt'

name = input("Please enter your name: \n")
address = input("Please enter your address: \n")
digits = input("Please enter your phone number: \n")

completePath = filePath + fileName

if os.path.exists(completePath):
    print("the path exists")
print(f"Saving to {completePath}")
print(completePath)

with open(completePath, 'w') as file_object:
    file_object.write(f"{name}, {address}, {digits}")

if os.path.exists(completePath):
    print("The path exists")

with open(completePath, 'r') as file_object:
    contents = file_object.read()
print(contents)

#C:\Users\Alex's Lenovo\Desktop\Python Work\