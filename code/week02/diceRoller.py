#diceRoller.py
#A program that can roll multiple dice of different sizes
#Author: Shane Austin

#imports the module 'random'
import random

num1 = int(input("What type of dice are you rolling 'd?': "))      #Request a number
num2 = int(input("How many dice are you rolling?: ")) 

number = random.randint(1,num1)
total = number * num2

print("{} d{} is: {}".format(num2, num1, total))