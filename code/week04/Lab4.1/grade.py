#grade.py
#A program that reads in a student mark and
#prints a grade
#Author: Shane Austin


percentage = float(input("Please enter the percentage mark:"))

#rounds the percentage to a full number
mark = round(percentage)

#if statement to check if it's a valid percentage
if mark < 0 or mark > 100:
    print("Please enter a valid percentage")

#elif boundaries for different grades
elif mark < 40 :
    print("Fail")

elif mark >= 40 and mark < 50:
    print("Pass")

elif mark >= 50 and mark < 60:
    print("Merit 2")

elif mark >= 60 and mark < 70:
    print("Merit 1")

elif mark >= 70:
    print("Distinction")


