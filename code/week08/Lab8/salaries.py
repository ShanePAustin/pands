#salaries.py
#A program that makes a list that generates 10 random numbers between 20000-80000
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

minSal = 20000
maxSal = 80000

numOfSal = 10

np.random.seed(1)
salaries = np.random.randint(minSal,maxSal,numOfSal)

bonusSal = salaries + 5000
incSal = salaries * 1.05

print(salaries)
print(bonusSal)
print(incSal)

plt.hist(salaries)
plt.show()