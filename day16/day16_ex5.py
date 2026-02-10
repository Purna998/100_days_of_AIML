# Use SVD to reduce the dimensionality of a dataset

# - Singular Value Decomposition (SVD) reduces dimensionality by projecting data onto directions 
# that capture the maximum variance, without explicitly computing the covariance matrix.


import numpy as np
import pandas as pd

df=pd.read_csv("iris.csv")

# Just taking numerical data
X=df.iloc[:,:-1].values

#Step 1: Mean-center the data
X_centered=X-np.mean(X,axis=0)

#Step 2: Apply SVD
U,S,VT=np.linalg.svd(X_centered,full_matrices=False)

#Step 3 : Choose top k components
k=2
Vk=VT[:k].T

# Project data to lower dimension
X_reduced=X_centered @ Vk
print(X_reduced.shape) # (m*n)

