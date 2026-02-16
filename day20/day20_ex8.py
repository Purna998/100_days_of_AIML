# Calculate confidence interval for a proportion
# Example: Proportion of students who scored ≥ 40 in exam_score

import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportion_confint

# Load dataset
df = pd.read_csv("student_exam_scores.csv")

# Define success condition (e.g., exam_score ≥ 40)
success = df[df['exam_score'] >= 40].shape[0]
n = df.shape[0]

# Sample proportion
p_hat = success / n

# Confidence level
confidence = 0.95
alpha = 1 - confidence

# Calculate confidence interval (Normal approximation method)
lower, upper = proportion_confint(count=success, nobs=n, alpha=alpha, method='normal')

print("Total Students:", n)
print("Number of students scoring ≥ 40:", success)
print("Sample Proportion:", round(p_hat, 4))
print(f"{int(confidence*100)}% Confidence Interval: ({round(lower,4)}, {round(upper,4)})")
