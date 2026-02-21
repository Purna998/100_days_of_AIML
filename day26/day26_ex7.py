# Use Real-World Datasets(e.g student scores by gender and class ) for hypothesis testing

# two way ANOVA
import statsmodels.api as sm
import pandas as pd
from statsmodels.formula.api import ols

# Create Dataset
data=pd.DataFrame({
    'Score':[
        78,82,85,80,76, # Male- Class A
        88,90,85,87,89, # Female- Class A

        72,75,70,68,74, # Male- Class B
        85,83,88,86,84, # Female - Class B

        90,92,88,91,89, # Male- Class C
        95,94,96,93,97, # Female- Class C
    ],
    'Gender':(['Male']*5+['Female']*5)*3,
    'Class':(['A']*10+['B']*10+['C']*10)

})

print(data.head())

# Fit model including interaction
model=ols("Score ~ C(Gender) + C(Class) + C(Gender):C(Class)",data=data).fit()

anova_table=sm.stats.anova_lm(model,typ=2)
print(anova_table)


import pandas as pd
import numpy as np
from scipy import stats
# Generate Dataset

# Simple dataset
data = pd.DataFrame({
    'Score': [78, 85, 69, 90, 72, 88, 95, 70],
    'Gender': ['Male', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Female', 'Male']
})

# Create Pass/Fail column
data['Result'] = ['Pass', 'Pass', 'Fail', 'Pass',
                  'Fail', 'Pass', 'Pass', 'Fail']


# Is Pass/Fail related to Gender?
# Chi-Square Test
table = pd.crosstab(data['Gender'], data['Result'])

chi2, p, dof, expected = stats.chi2_contingency(table)

print("Contingency Table:\n", table)
print("Chi-Square Statistic:", chi2)
print("P-Value:", p)

#Is the average score different from 75?
# Z-test
mean = np.mean(data['Score'])
mu = 75
std = np.std(data['Score'], ddof=1)
n = len(data['Score'])

z_stat = (mean - mu) / (std / np.sqrt(n))
p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))

print("Z-Statistic:", z_stat)
print("P-Value:", p_value)

# Do male and female students have different average scores?
# T-Test
male_scores = data[data['Gender'] == 'Male']['Score']
female_scores = data[data['Gender'] == 'Female']['Score']

t_stat, p_value = stats.ttest_ind(male_scores, female_scores)

print("T-Statistic:", t_stat)
print("P-Value:", p_value)