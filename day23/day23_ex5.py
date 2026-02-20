import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# PART 1: Normal Distribution (Height Dataset)

df = pd.read_csv("SOCR-HeightWeight.csv")

heights = df["Height(Inches)"]

mean = heights.mean()
std = heights.std()

print("Mean Height:", mean)
print("Standard Deviation:", std)

plt.hist(heights, bins=30, density=True, alpha=0.6)

x = np.linspace(heights.min(), heights.max(), 100)
y = norm.pdf(x, mean, std)

plt.plot(x, y)
plt.title("Normal Distribution Fit for Human Height")
plt.xlabel("Height (Inches)")
plt.ylabel("Density")
plt.show()

# PART 2: Binomial Distribution (Coin Toss)

# Simulate 10000 experiments of 10 coin tosses
n = 10        # number of trials
p = 0.5       # probability of head
size = 10000  # number of experiments

# Generate binomial data
tosses = np.random.binomial(n, p, size)

print("First 20 outcomes:", tosses[:20])

# Plot histogram
plt.hist(tosses, bins=range(n+2), density=True, alpha=0.6)

# Theoretical binomial PMF
x = np.arange(0, n+1)
y = binom.pmf(x, n, p)

plt.plot(x, y, marker='o')
plt.title("Binomial Distribution (10 Coin Tosses)")
plt.xlabel("Number of Heads")
plt.ylabel("Probability")
plt.show()
