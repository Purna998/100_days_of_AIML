# Use another dataset and apply the same EDA steps
# Explore advanced visualizations like boxplots or pairplots in Seaborn

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
df=pd.read_csv("iris.csv")
print(df.head())
print(df.info())
print(df.describe())
df.drop_duplicates()

# Bar Chart : Species vs sepal_length
plt.barh(df['species'],df['sepal_length'],color="purple")
plt.title("Bar Chart")
plt.show()

# Scatter plot: Sepal_length vs Petal Length
plt.scatter(df['sepal_length'],df['petal_width'])
plt.title("Scatter Plot")
plt.show()

# Box plot: Outliers Detection
plt.boxplot(df['sepal_length'])
plt.title("Box plot")
plt.show()

# Pair plot
sns.pairplot(df)
plt.title("Pairplot")
plt.show()

