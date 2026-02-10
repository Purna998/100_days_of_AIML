# Compute eigenvalues and eigenvectors for larger matrices
import numpy as np
import pandas as pd

df=pd.read_csv("iris.csv")

# Eigen values and vectors works only on square data like 3*3 but iris is 150*4 so, we have use this
X=df.iloc[:,:-1]

# Mean center the data
X_centered=X-np.mean(X,axis=0)

# Compute Covariance
cov_mat=np.cov(X_centered,rowvar=False) 
# Cov > 0 → both variables increase or decrease together
# Cov < 0 → one increases while the other decreases
# Cov = 0 → no linear relationship

# Eigen decomposition
eigenval,eigenvec=np.linalg.eig(cov_mat)

print("Eigen Values:\n",eigenval)
print("Eigen Vectors:\n",eigenvec)
