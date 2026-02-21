# Chi-Square Test
from scipy.stats import chi2_contingency

# Contingency Table
data=[[50,30],[20,40]]

# Perform Chi-square test
chi2,p,dof,expected=chi2_contingency(data)
print("Chi-Square Statistics: ",chi2)
print("P-value: ",p)
print("Expected Frequecies: ",expected)