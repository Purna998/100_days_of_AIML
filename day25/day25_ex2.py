# Two Sample T-Test
import numpy as np
from scipy.stats import ttest_ind

# Data From two groups 
group1=[12,14,15,16,18,19]
group2=[11,13,14,15,16,17,18]

# Perform t-test 
t_stat,p_value=ttest_ind(group1,group2)
print("T-statistic: ",t_stat)
print("P-value: ",p_value)

# Interpretation
alpha=0.05
if p_value<=alpha:
    print("Reject the null hypothesis: significant difference")
else:
    print("Reject the null hypothesis: No significant difference")
