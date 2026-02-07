# Create a histogram with multiple datasets overlaid

import matplotlib.pyplot as plt
import numpy as np

x = [3,4,2,7,5,4,4,3,3,3,3,8,7,8]
y = [4,3,3,2,6,6,3,3,1,2,9,9,4,5]

plt.hist(x, bins=4, alpha=0.6, label='Dataset X', edgecolor='black')
plt.hist(y, bins=4, alpha=0.6, label='Dataset Y', edgecolor='black')

plt.legend()
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Overlaid Histograms")
plt.show()
