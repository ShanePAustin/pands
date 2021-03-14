#agePlot.py
#A program that makes a list that generates 10 random ages between 21-65 and creates a scatter plot
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

minSal = 20000
maxSal = 80000


minAge = 21
maxAge = 65

num = 10

np.random.seed(1)
salaries = np.random.randint(minSal,maxSal,num)
ages = np.random.randint(minAge,maxAge,num)


plt.scatter(ages, salaries, label = "salaries")


xpoints = np.array(range(21,65))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, color = 'g', label = "x squared")

plt.title ("Salaries Plot")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.legend()
#plt.show()
plt.savefig("prettier-plot.png")
