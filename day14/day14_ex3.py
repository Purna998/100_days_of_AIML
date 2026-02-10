# Generate visualizations to illustrate key insights
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Titanic Dataset
# df=sns.load_dataset("titanic")
df=pd.read_csv("Titanic-Dataset.csv")
print(df.head())

# Bar Chart: Survival rate by class
survival_by_class=df.groupby("Pclass")["Survived"].mean() # Mean values of survived passenger on the basis passenger classes
print("Survival by Class:\n",survival_by_class)
survival_by_class.plot(kind="bar",color="skyblue")
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")
plt.show()

# # Histogram Age Distribution
sns.histplot(df["Age"], bins=20,kde=True,color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# # BarChart: Survived on the basis of Sex
survived_by_age=df.groupby("Sex")["Survived"].mean()
survived_by_age.plot(kind="bar",color="skyblue")
plt.title("Survival Rate by Sex")
plt.ylabel("Survival Rate")
plt.xlabel("Sex")
plt.show()

# df.dropna()
correlation_matrix=df.iloc[0:4]
correlation_matrix.corr()
sns.heatmap(correlation_matrix,annot=True,cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# Scatter Plot: Age vs Fare
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()