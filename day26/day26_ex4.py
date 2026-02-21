# 2. Perform a chi-square test
# 3. Conduct ANOVA

# Chi-Square Test: Test the independence of categorical data
from scipy.stats import chi2_contingency

# Contingency Table
data=[[50,30,20],[30,40,30]]

# Perform the chisquare
chi2,p,dof,expected=chi2_contingency(data)
print("Chi-Square Statistic: ",chi2)
print("P-value: ",p)
print("Expected Frequencies: ",expected)
