# Hypothesis Testing
# Perform a hypothesis test
import numpy as np
from scipy.stats import ttest_1samp

# Sample data
data=[12,14,15,16,17,18,19]

# Null Hypothesis: mean=15
population_mean=15

# Perform t-test
alpha=0.5
if p_value<=alpha:
    print("Reject the null hypothesis: Significant difference")
else:
    print("Fail to Reject the null hypothesis: No significant difference")
