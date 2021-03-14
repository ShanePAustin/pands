#plot.py
#A program that plots the function y = x*x
#Author: Shane Austin

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)

plt.show()