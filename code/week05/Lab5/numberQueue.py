#numberQueue.py
#A program that generates 10 numbers and ouputs them in a queue
#Shane Austin

import random

numbers = []
number = random.randint(1,101)

for i in range(0,10):
    numbers.append(random.randint(0,100))

print ("Queue is {} ".format(numbers))

while len(numbers) != 0:
    nextNumber = numbers.pop(0)
    print ("Current Number is {} and the queue is {}" .format(nextNumber, numbers))

print ("The queue is now empty")