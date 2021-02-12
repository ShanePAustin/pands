#binaryCalc.py
#A program that takes in an integer and outputs it in binary
#Author: Shane Austin

DateRemainder = []

num1 = int(input("Please enter a positive integer: "))

while num1 != 0:

    print(num1,"/2 =",int(num1//2),"(",num1%2,");", end = " ")

    remainder = (num1 % 2)
    DateRemainder.append(remainder)
    num1 = (num1 // 2)
   
 
print('\n',DateRemainder[::-1])



    