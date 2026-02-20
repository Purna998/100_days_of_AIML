# Compare the effects of skewness and kurtosis on different

from scipy.stats import skew,kurtosis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Dataset
df=pd.read_csv("iris.csv")

# Taking sepal_length as feature
feature=df['sepal_length']
# Skewness
print("Skewness of sepal_length: ",skew(feature))
print("Kurtosis of petal_length: ",kurtosis(feature))
sns.histplot(feature, kde=True)
plt.title("Sepal Length Distribution")
plt.show()

# Taking petal_length as feature
feature=df['petal_length']
print("Skewness of petal_length: ",skew(feature))
print("Kurtosis of petal_length: ",kurtosis(feature))
sns.histplot(feature, kde=True)
plt.title("Petal Length Distribution")
plt.show()



