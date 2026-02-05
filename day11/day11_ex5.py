# Drop Columns with more than 50% missing values
import numpy as np
import pandas as pd

# load dataset
df=pd.DataFrame({
    "Name":["Alice","Joseph","John","Roman","Allen"],
    "Age":[45,32,56,38,13],
    "Score":[78,98,70,89,81],
    "BMI":[12,np.nan,11,np.nan,np.nan]
})
print("Original Dataset:\n",df)

# threshold=50% of rows
threshold=len(df)*0.5
df=df.dropna(axis=1,thresh=threshold)

print("\nAfter dropping columns with >50% missing values:\n",df)