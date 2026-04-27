# a module is a file that contains the definition of functions,
# classes, and variables that can be used in other programs. 
# Importing alows you to acess the functionality and 
# reuse the code efficiently, as well as create your own module

import math 

print("Square root")
result = math.sqrt(25)
print(result)

#another way to do this is 
# import math sqrt
# result = sqrt(25)
# print(result) # printed = 5

# some import examples

import random
import datetime

print("\nA random number: ")
random_num = random.randint(1, 6)
print(random_num)

print("\nA actual time and data")
actual_date = datetime.datetime.now()
print(actual_date)
