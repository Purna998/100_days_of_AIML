# Implement Matrix-vector Multiplication

import numpy as np

# Create Matrices
M=np.array([[1,2,3],[4,5,6],[7,8,9]])
v=np.array([1,0,-1])

# Matrix-vector Multiplication
result=np.dot(M,v)
print("Matrix Vector Multiplication:\n",result)

