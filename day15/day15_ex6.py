# Create a block diagonal matrix using numpy 
import numpy as np
import scipy as sp
# Define your input matrices (can be of different sizes)
A = np.array([[1, 2], 
              [3, 4]])
B = np.array([[5, 6, 7], 
              [8, 9, 10],
              [11, 12, 13]])
C = np.array([[14]])

block_diagonal=sp.linalg.block_diag(A,B,C)
print("Block Diagonal Matrix:\n", block_diagonal)