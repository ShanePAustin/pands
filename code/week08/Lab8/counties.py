#counties.py
#A program that makes a list of counties assigns a value to them and plots a barchart
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

connacht = np.array(["Galway", "Sligo", "Mayo", "Leitrim", "Roscommon"])


num = 20

np.random.seed(1)
championships = np.random.randint(1,num,5)

print (championships)

plt.bar( connacht, championships)
plt.title ("Championships")
#plt.legend()
#plt.show()
plt.savefig("ConnachtChampionships.png")



