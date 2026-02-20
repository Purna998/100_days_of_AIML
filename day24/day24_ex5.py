# Perform stratified sampling and compare intervals across strata

import numpy as np
from scipy.stats import t

# Simulated data
np.random.seed(42)
male_scores = np.random.normal(loc=75, scale=10, size=50)   # stratum 1
female_scores = np.random.normal(loc=80, scale=12, size=50) # stratum 2

# Function to compute mean CI
def mean_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    sem = np.std(data, ddof=1) / np.sqrt(n)  # standard error
    h = sem * t.ppf((1 + confidence) / 2, n - 1)
    return mean, mean - h, mean + h

# Compute CI for each stratum
male_mean, male_lower, male_upper = mean_confidence_interval(male_scores)
female_mean, female_lower, female_upper = mean_confidence_interval(female_scores)

print(f"Male: mean={male_mean:.2f}, 95% CI=({male_lower:.2f}, {male_upper:.2f})")
print(f"Female: mean={female_mean:.2f}, 95% CI=({female_lower:.2f}, {female_upper:.2f})")
