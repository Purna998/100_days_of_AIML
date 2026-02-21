from day26_ex7 import *

# Box plot of t-test
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(6,4))
sns.boxplot(x='Gender', y='Score', data=data)

plt.title("T-Test Visualization: Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Score")

plt.show()