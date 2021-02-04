#normalise.py
#This is a program that reads in a string and strips any leading or 
# trailing spaces, the program also converts the string to lower case.
#and output the length of the input and output strings.
#Author: Shane Austin

string = input("Enter a String: ")

#Take string and convert to lower case and trim
normString = string.lower().strip()                 

#Count length of Strings
lengthOfString = len(string)
lengthOfNormString = len(normString)

#/n for a new line in code
print(("That String normalised is: {} \n We reduced the input string from {} to {} characters").format(normString, lengthOfString, lengthOfNormString))
