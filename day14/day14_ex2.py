# Perform Data Cleaning, Aggregation and Filtering
import pandas as pd

# Load Titanic Dataset
# df=sns.load_dataset("titanic")
df=pd.read_csv("Titanic-Dataset.csv")

print(df.head())

# Inspect Data
print(df.info())
print(df.describe())

# Handle Missing Values
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode())

# Remove duplicates 
df=df.drop_duplicates()

# Filter data: Passengers in first class
first_class=df[df["Pclass"]==1]
print("First Class Passengers:\n",first_class.head())