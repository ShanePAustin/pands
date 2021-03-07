#es.py
#A program that reads in a text file and outputs the number of e's it contains
#Author: Shane Austin

import sys

filename = sys.argv[1]

def countEs():

    with open (filename) as f:
        content = f.read()
        Es = content.count("e")
       
        return Es

howManyEs = countEs()
print ("There are {} 'E's' in {}".format(howManyEs,filename))