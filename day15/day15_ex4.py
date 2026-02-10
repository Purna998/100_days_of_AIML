# Compute the determinant and inverse of a 2*2 Matrix using Numpy 

import numpy as np

# Create 2*2 Matrix
A=np.array([[1,2],[3,4]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])

# Determinant of 2*2 Matrix A
det_A=np.linalg.det(A)
det_B=np.linalg.det(B)

print("Determinant of 2*2 Matrix A:\n",det_A)
print("Determinant of 3*3 Matrix B:\n",det_B)

# Inverse of Matrix
inv_A=np.linalg.inv(A)
# inv_B=np.linalg.inv(B)

print("Inverse of 2*2 Matrix A:\n",inv_A)
# print("Inverse of 3*3 Matrix B",inv_B)
