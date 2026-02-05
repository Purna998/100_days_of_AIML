# Import libraries
import pandas as pd

# Explore Iris Dataset
df=pd.read_csv("iris.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print("Shape: \n",df.shape)

# create a dataframe from a dictionary and add a new calculated column
df['sepal_area']=df['sepal_length']*df['sepal_width']
print(df.head())
df.to_csv('iris_sepal_area_added.csv',index=False)