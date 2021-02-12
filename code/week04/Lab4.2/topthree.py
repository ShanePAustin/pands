#topthree.py
#A program that creates 10 random numbers and prints them out
#and prints the top three
#Author: Shane Austin

import random

numbers = []

for i in range(0,10):
    numbers.append(random.randint(0,100))

print ("{} random numbers\t {}" .format(10,numbers))

numbers.sort(reverse = True)

print ("The top 3 are \t\t {}" .format(numbers[0:3]))

