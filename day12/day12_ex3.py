# Group Data by a categorical column
import pandas as pd

data={
    "class":["A","B","A","B","C","C"],
    "Score":[85,90,88,72,95,80],
    "Age":[15,16,15,17,16,15],
}

df=pd.DataFrame(data)

print("Original Dataset:\n",df)

grouped=df.groupby("class").mean() # On the basis of class A, B and C it calculate the mean
print(grouped)