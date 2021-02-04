#randomGenerator.py
#A program that generates a random number between a given range
#Author: Shane Austin

#imports the module 'random'
import random

num1 = int(input("Enter first number: "))      #Request a number
num2 = int(input("Enter second number: ")) 

number = random.randint(num1,num2)

print("A random number between {} and {} is: {}".format(num1, num2, number))