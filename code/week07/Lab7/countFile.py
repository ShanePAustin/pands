#countFile.py
#A program that counts how many times a file was run
#Author: Shane Austin

filename = "count.txt"

def readNumber():

    with open (filename) as f:
        number = int(f.read())
        return number

def writeNumber(number):
    with open (filename, "wt") as f:
        f.write(str(number))


num = readNumber()
num += 1
print ("We have run this program {} times".format(num))
writeNumber(num)

