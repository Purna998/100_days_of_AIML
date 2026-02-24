# Exercise 1: Calculate Correlation Between Features
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris Dataset
df=pd.read_csv("iris.csv")

# Compute correlation matrix
df=df.iloc[:,:-1]
correlation_matrix=df.corr()

# Plot Heatmap
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Feature Correlations")
plt.show()