#initFile.py
#A program that initialises a file
#Author: Shane Austin

import os.path

filename = "count.txt"

if not os.path.isfile(filename):
    print("File does not exist")
    writeNumber(0)

def readNumber():
    try:
        with open (filename) as f:
            number = int(f.read())
            return number
    except IOError:

        return 0

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))


num = readNumber()
num += 1
print ("We have run this program {} times".format(num))
writeNumber(num)
