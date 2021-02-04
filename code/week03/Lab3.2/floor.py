#floor.py
#A program that takes a number and returns an int rounded down

import math

num1 = float(input("Enter a float number:- "))
floor = math.floor(num1) 

print("{} floored is {}".format(num1, floor))