# Vectors and Matrices
import numpy as np

A = np.array([[1,2],[3,5]])
B = np.array([[5,6],[7,8]])

# Addition and Matrices
print("Addition:\n",A+B)
print("Subtraction:\n",A-B)

# Scalar Multiplication
C=2*A
print("Scalar Multiplication:\n",C)

# Matrix Multiplication
multiply=np.dot(A,B)
print("Matrix Multiplication:\n",multiply)

# Special Matrix
# 1. Identity Matrix
I=np.eye(3)
print("Identity Matrix:\n",I)

# 2. Zero Matrix
Z=np.zeros((2,3))
print("Zero Matrix:\n",Z)

# 3.Diagonal Matrix(Always Square Matrix)
D=np.diag([1,2,3])
print("Diagonal Matrix:\n",D)