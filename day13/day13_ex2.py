# Seaborn - More advanced visualization tool than matplotlib but built in matplotlib
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data=np.random.rand(5,5)
# sns.heatmap(data,annot=True,cmap="coolwarm")
# plt.title("Heatmap")
sns.pairplot(df)
plt.show()
