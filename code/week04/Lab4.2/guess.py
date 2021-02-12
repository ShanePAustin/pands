#guess.py
#A program that makes you guess a random number
#Author: Shane Austin

import random

num1 = random.randint(1,101)

guess = int(input("Please guess the number between 1 and 100:"))

while guess != num1:
    
    if guess < num1: 
        print ("Too Low")

    else: 
        print("Too High")

    guess = int(input("Guess again: "))

print ("Well done! Yes the number was ",num1)