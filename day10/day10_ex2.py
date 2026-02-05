import pandas as pd
# load dataset using files
df=pd.read_csv("data.csv")
df=pd.read_excel("data.xlsx")
# Save to files
df.to_csv("data.csv",index=False) #if we don't want to save index/s.n
df.to_excel("data.xlsx")

# Viewing Data
print(df.head())
pritn(df.tail(3))
# Statistical data
print(df.info())
print(df.describe())

print(df["Name"]) # Selecting Single columns
print(df["Name","Age"])

print(df[df["Age"]>25]) # Filtering rows of age greater than 25

print(df.iloc[0]) # Selecting columns by position
print(df.iloc[:,0])

print(df.loc[0]) 
print(df.loc[:,"Name"])  # selecting columns by label "Name"

