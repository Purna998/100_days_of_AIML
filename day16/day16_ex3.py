 # Matrix Decomposition using singular value decompostion
import numpy as np

A = np.array([[3,1,1],[-1,3,1],[1,1,3]])
U,S,Vt=np.linalg.svd(A)

print("U:\n",U)
print("Singular Values:\n",S)
print("V Transpose:\n",Vt)

# Reconstruct 
sigma=np.zeros((3,3))
np.fill_diagonal(sigma,S)
reconstructed=U @ sigma @ Vt #@ symbol is the matrix multiplication operator in Python
print("Reconstructed Matrix\n",reconstructed)