# use the iris dataset to test if the mean sepal length differs between two species

import numpy as np
import pandas as pd
from scipy.stats import norm

# Load dataset
df = pd.read_csv("../day24/iris.csv")

# Select two species
species1 = df[df['species'] == 'setosa']['sepal_length']
species2 = df[df['species'] == 'versicolor']['sepal_length']

# Sample sizes
n1 = len(species1)
n2 = len(species2)

# Means
mean1 = species1.mean()
mean2 = species2.mean()

# Standard deviations
std1 = species1.std(ddof=1)
std2 = species2.std(ddof=1)

# Standard error for difference in means
std_error = np.sqrt((std1**2 / n1) + (std2**2 / n2))

# Z statistic
z_value = (mean1 - mean2) / std_error

# Two-tailed p-value
p_value = 2 * (1 - norm.cdf(abs(z_value)))

print("Z-value:", z_value)
print("P-value:", p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothesis: Significant difference between species")
else:
    print("Fail to reject the null hypothesis: No significant difference between species")