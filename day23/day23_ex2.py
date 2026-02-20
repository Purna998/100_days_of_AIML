from scipy.stats import skew, kurtosis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df=pd.read_csv("iris.csv")

# Analyse Sepal_length
feature=df['sepal_length']
print("Skewness: ",skew(feature))
print("Kurtosis: ",kurtosis(feature))

# Visualize distribution
sns.histplot(feature,kde=True)
plt.title("Distribution of Sepal Length")
plt.show()