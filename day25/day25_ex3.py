# Perform a z-test for large sample sizes
import numpy as np
from scipy.stats import norm

np.random.seed(42)

# Generate population data
data = np.random.randint(1, 50000, size=1000)

# Hypothesized population mean
population_mean = data.mean()

# Random sample
samples = np.random.choice(data, size=50, replace=False)

# Sample statistics
sample_mean = samples.mean()
sample_std = samples.std(ddof=1)

# Standard error (using sample std)
standard_error = sample_std / np.sqrt(len(samples))

# Z statistic
z_stat = (sample_mean - population_mean) / standard_error

# Two-tailed p-value
p_value = 2 * (1 - norm.cdf(abs(z_stat)))

print("Z-statistic:", z_stat)
print("P-value:", p_value)

alpha = 0.05

if p_value <= alpha:
    print("Reject the null hypothesis: Significant difference")
else:
    print("Fail to reject the null hypothesis: No significant difference")