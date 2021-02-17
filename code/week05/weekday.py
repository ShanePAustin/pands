#weekday.py
#A program that outputs whether or not today is a weekday.
#Author: Shane Austin

import datetime

time = datetime.datetime.now()

today = (time.strftime("%A"))


if (today == 'Saturday' or today == 'Sunday'):
    print("It is the weekend, yay!")

else:
    print ("Yes, unfortunately today is a weekday.")
