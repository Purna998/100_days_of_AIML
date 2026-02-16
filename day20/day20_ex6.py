# Visualize the distribution of data and highlight mean, median, and mode using matplotlib

import numpy as np
import matplotlib.pyplot as plt
from statistics import mode

# Create data
data = [10, 20, 30, 40, 50, 20, 30, 20]

# Calculate statistics
mean_val = np.mean(data)
median_val = np.median(data)
mode_val = mode(data)

# Create figure
plt.figure()

# Boxplot
plt.boxplot(data, vert=False)

# Highlight mean, median, and mode
plt.scatter(mean_val, 1, color='red', label=f"Mean: {mean_val}")
plt.scatter(median_val, 1, color='green', label=f"Median: {median_val}")
plt.scatter(mode_val, 1, color='blue', label=f"Mode: {mode_val}")

plt.title("Box Plot with Mean, Median, and Mode")
plt.yticks([])
plt.legend()
plt.show()
