#pallindrome.py
# A program that asks a user to input a string and says if it is a pallindrome.
#Author: Shane Austin

inputString = input("Please enter a sentence: ")

#Takes the inputted string and reverses by slicing with [::-1]
newString = inputString[::-1]

print("That is a Pallindrome" if(inputString == newString) else "That is not a pallindrome")
