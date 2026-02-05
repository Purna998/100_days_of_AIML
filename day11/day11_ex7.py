# Convert categorical data to numerical using one-hot encoding
import numpy as np
import pandas as pd

df=pd.DataFrame({
    "Age":[54,64,32,43,58],
    "Salary":[45000,80000,23000,50000,34000],
    "Loan":["yes","yes","no","yes","no"]
})

print("Original Dataset:\n",df)

# Label Encoding
df['Loan']=df['Loan'].replace({'yes':1,'no':0})
print("After Label encoding: ",df)

# One hot encoding
df_encoded=pd.get_dummies(df,columns=["Loan"]) # to avoid dummy variable trap use drop_first=True parameter
print("\nAfter One-Hot Encoding:\n",df_encoded)