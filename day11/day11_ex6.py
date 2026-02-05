# Merge three datasets and analyze relationships between them 
import numpy as np
import pandas as pd

# Dataset 1: Personal details
df1 = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Joseph", "John", "Roman", "Allen"],
    "Age": [45, 32, 56, 38, 13],
    "Score": [78, 98, 70, 89, 81],
    "BMI": [12, np.nan, 11, np.nan, np.nan]
})

# Dataset 2: Academic details
df2 = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "College": ["LTU", "MMC", "BBC", "SMC", "LTU"],
    "RollNo": [4, 15, 12, 3, 8]
})

# Dataset 3: Attendance details
df3 = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Attendance": [85, 92, 78, 88, 90]
})

merged_df=pd.merge(df1,df2,how="inner",on="ID")
print("\nAfter merge dataset 1 and dataset 2: \n",merged_df)

merged_df=pd.merge(merged_df,df3,how="inner",on="ID")
print("Merged Dataset:\n", merged_df)

print("\nCorrelation Matrix:\n")
print(merged_df[["Age", "Score", "BMI", "Attendance"]].corr())


print("\nAverage Score by College:\n")
print(merged_df.groupby("College")["Score"].mean())

print("\nAttendance vs Score:\n")
print(merged_df[["Attendance", "Score"]])