# Hands on Exercise- Create a Heatmap with seaborn
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Iris dataset
df=sns.load_dataset("iris")

# Calculate the correlation matrix
df=df.iloc[:,:-1]
correlation_matrix=df.corr()

# Plot heatmap
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
