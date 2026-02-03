# Broadcasting in Numpy:Broadcasting in NumPy allows us to perform arithmetic operations on arrays of different shapes without reshaping them.
# Rules of Broadcasting
# -Dimensions are aligned from the right
# -A dimension is compatible if:
# -- It matches the other array's dimension
# -- One of the dimensions is 1
import numpy as np

# Array and Scalar broadcasting
arr=np.array([1,2,3])
print(arr+10)

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([1,0,1])
print(matrix+vector)