# # Performing Exploratory Data Analysis (EDA)
#     # Steps in EDA 
#         # Load and inspect the dataset
#         # Check for missing or inconsistent data
#         # Visualize distributions and relationships using histograms, scatter plots and correlation heatmaps
# # Key Goals
#     # Understand the data structure 
#     # Identify patterns, trends and 
# EDA
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

# # Load Dataset
df=pd.read_csv("tips.csv")

# # Inspect Data
print(df.info())
print(df.describe())

del df["Payment ID"]
del df["CC Number"]
del df["Payer Name"]
del df["sex"]
del df["smoker"]
del df["day"]
del df["price_per_person"]
del df["time"]


# # Visualize Distributions
sns.histplot(df["total_bill"],kde=True)
plt.title("Distribution of Total Bill")
plt.show()
print(df.head())
# # Correlation heat map
sns.heatmap(df.corr(),annot=True,cmap="coolwarm")
plt.show()



