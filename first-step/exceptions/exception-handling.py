print("Try")
#code that could throw an exception
#if an exception occurs in the try block, 
#the flow of execution is trasferred to the corresponding except block

try:
    result = 10/1
    print(result)
except ZeroDivisionError:
    print("ERROR: Zero Division")

print("\nExcept")
#specifies the type of exception you want to validate,
#you can have a multiple blocks to handle different exception types 

try:
    result = 10/0
    print(result)
except ZeroDivisionError:
    print("ERROR: Zero Division")
except ValueError:
    print("ERROR: Invalid Value")

print("\nFinally")
#optional and always executed, regardless of whether there was an exception or not, 
#used in cleanup tasks or resource release

try:
    file = open("file.txt", "r")
except FileNotFoundError:
    print("ERROR: File Not Found")
finally:
    file.close()
#an error occurred because file.txt does not exist. 
