# Load and Explore the dataset
import seaborn as sns
import pandas as pd
from seaborn import load_dataset

# Load Dataset
df=sns.load_dataset('iris')
# print(df)

# Explore structure
# print("First 5 rows:\n",df.head())
# print("First 5 rows:\n",df.tail())

# print(df.info())
# print(df.describe())

# Select Specific columns and filter rows

species_col=df[["species"]]
print(species_col)

#Filtering rows
filtered_rows=df[(df["sepal_length"]>5.0) & (df["species"]=="setosa")]
print("Filtered Rows:\n",filtered_rows)

