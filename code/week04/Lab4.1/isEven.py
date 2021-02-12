#isEven.py
#A program that asks the user to enter in a number, and the
#tells the user if the number is even or odd.
#Author: Shane Austin


num1 = int(input("Please Enter a Number: (-1 to quit)"))

while num1 != -1:

    if (num1 % 2) == 0 :
        print("{} is an even number" .format(num1))

    else: 
        print("{} is an odd number" .format(num1))
    
    num1 = int(input("Please Enter another Number:"))

print("Goodbye")