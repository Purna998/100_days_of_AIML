# Perform Two Way Anova to test for interaction effects
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

data = pd.DataFrame({
    'Value': [
        10,11, 12,13, 14,15, 16,17, 18,19,      # G1
        9,10, 11,12, 13,14, 15,16, 17,18,       # G2
        8,9, 10,11, 12,13, 14,15, 16,17         # G3
    ],
    'Group': ['G1']*10 + ['G2']*10 + ['G3']*10,
    'Time': ['T1','T1','T2','T2','T3','T3','T4','T4','T5','T5']*3
})

model = ols('Value ~ C(Group) * C(Time)', data=data).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

# 🔎 Explanation

# C(Group) → Main effect of Group
# C(Time) → Main effect of Time
# C(Group):C(Time) → Interaction effect
# typ=2 → Type II Sum of Squares (commonly used)

# 🧠 Interpreting Results
# From the ANOVA table:
# PR(>F) column gives the p-values.
# If:
# p < 0.05 for C(Group) → Significant group effect
# p < 0.05 for C(Time) → Significant time effect
# p < 0.05 for C(Group):C(Time) → Significant interaction effect
# If interaction is significant → The effect of Group depends on Time.