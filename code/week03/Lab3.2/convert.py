#convert.py
#A program that takes a number and convets to cents
#Author: Shane Austin

num1 = float(input("Please enter an amount: "))
cent = round(num1 * 100)
absoluteValue = abs(cent)


print("That amount in cent is: {}" .format(absoluteValue))