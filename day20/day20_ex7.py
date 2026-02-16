# Hypothesis Testing using the given dataset
# Example: Compare exam scores of students who study < 6 hours vs ≥ 6 hours

import pandas as pd
from scipy.stats import ttest_ind

# Load dataset
df = pd.read_csv("student_exam_scores.csv")

# Create two groups based on hours studied
group1 = df[df['hours_studied'] < 6]['exam_score']
group2 = df[df['hours_studied'] >= 6]['exam_score']

# Perform Independent T-Test
t_stat, p_value = ttest_ind(group1, group2)

print("Number of students (Study < 6 hrs):", len(group1))
print("Number of students (Study ≥ 6 hrs):", len(group2))
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpretation
alpha = 0.05  # 5% significance level

if p_value < alpha:
    print("Reject the null hypothesis: Significant difference in exam scores.")
else:
    print("Failed to reject the null hypothesis: No significant difference in exam scores.")
