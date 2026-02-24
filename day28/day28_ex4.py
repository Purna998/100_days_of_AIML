# Statistical Analysis of Real-World Data
import matplotlib.pyplot as plt 
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load Dataset
df=pd.read_csv("tips.csv")

contingency_table=pd.crosstab(df['smoker'],df['time'])

# Perform Ch-Square Test
chi2,p,dof,expected=chi2_contingency(contingency_table)
print("Chi-Square Statistic: ",chi2)
print("P-Value: ",p)

# Interpret Result
alpha=0.05
if p <=alpha:
    print("Reject the null hypothesis: Variables are dependent")
else:
    print("Fail to reject the null hypothesis: Variables are independent")
    