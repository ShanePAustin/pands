#randomFruit.py
#A program that outputs a random fruit
#Author: Shane Austin

#imports the module 'random'
import random

fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape")
pick = random.randint(0,len(fruits)-1)

fruit = fruits[pick]

print("A random fruit is: {}".format(fruit))