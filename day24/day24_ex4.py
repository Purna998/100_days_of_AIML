# Create confidence intervals for other statistics

import numpy as np
from scipy.stats import chi2

# Example dataset
data = np.array([12, 15, 14, 10, 13, 16, 18, 11, 17, 14])

# Sample size
n = len(data)

# Sample variance (unbiased, ddof=1)
s2 = np.var(data, ddof=1)

# Confidence level
confidence = 0.95
alpha = 1 - confidence

# Degrees of freedom
df = n - 1

# Chi-square critical values
chi2_lower = chi2.ppf(alpha / 2, df)
chi2_upper = chi2.ppf(1 - alpha / 2, df)

# Confidence interval for variance
lower_var = (df * s2) / chi2_upper
upper_var = (df * s2) / chi2_lower

# Confidence interval for standard deviation
lower_std = np.sqrt(lower_var)
upper_std = np.sqrt(upper_var)

print("Sample variance:", s2)
print(f"{confidence*100}% CI for variance:", (lower_var, upper_var))
print(f"{confidence*100}% CI for standard deviation:", (lower_std, upper_std))
