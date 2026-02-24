# Hypothesis testing ttest
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# # Load Dataset
df=pd.read_csv("tips.csv")
# Conducting Hypothesis Testing
from scipy.stats import ttest_ind

# Separate data by gender
male_tips=df[df['sex']=='Male']['tip']
female_tips=df[df['sex']=='Female']['tip']

# Perform t-test
t_stat,p_value=ttest_ind(male_tips,female_tips)
print("T-statistics: ",t_stat)
print("P-Value: ",p_value)

# Interpret Results
alpha=0.05
if p_value<=alpha:
    print("Reject all null hypothesis: Significant difference.")
else:
    print("Fail to Reject all null hypothesis: No Significant Difference.")