# Create a 3*3 Matrix and perform operations
import numpy as np

matrix1=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
matrix2=np.array([
    [9,8,7],
    [6,5,4],
    [3,2,1]
])
print("Original Matrix:\n",matrix1)

# Transpose
transpose=matrix1.T
print("\nTranspose:\n",transpose)

#addition of matrix
print("\nAddition:\n",matrix1+matrix2)
print("\Multiplication:\n",matrix1*matrix2)