# Use seaborn to create a violin plot or box plot for visualizing distributions
import seaborn as sns
import matplotlib.pyplot as plt

x=[1,23,34,12,54,112,36,20,12,10,45,44,21]
sns.boxplot(x=x)
plt.title("Boxplot")
plt.show()

sns.violinplot(x=x)
plt.show()