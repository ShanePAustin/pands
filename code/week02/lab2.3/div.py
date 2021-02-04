#div.py
#A division program that returns a remainder
#Author: Shane Austin

num1 = int(input("Enter first number: "))                       #Request a number
num2 = int(input("Enter the number you want to divide by: ")) 

answer = int(num1 // num2)
remainder = num1 % num2                                         #Gives mod remainder     

print("{} divided by {} is {} with remaider {}".format(num1, num2, answer, remainder))