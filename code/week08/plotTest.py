#plotTest.py
#A program that plots the function x, x^2 and x^3
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(0,4))


fx = xpoints
gx = xpoints**2
hx = xpoints**3

plt.plot(xpoints, fx)
plt.plot(xpoints, gx)
plt.plot(xpoints, hx)

#plt.show()
plt.savefig("plotTest.png")