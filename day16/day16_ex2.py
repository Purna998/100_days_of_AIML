# Eigen Values and Vectors

import numpy as np

A=np.array([[2,3],[1,4]])

eigenvalues,eigenvectors=np.linalg.eig(A)
# print("EigenVal\n:",eigenvalues)
# print("EigenVectors\n:",eigenvectors)

B=np.array([[4,2],[1,1]])
eigval,eigvec=np.linalg.eig(B)
print("EigVal:",eigval)
print("EigVec:\n",eigvec)

# Matrix Decomposition: Singular value decomposition(SVD)
U,S,Vt=np.linalg.svd(A)
print("U:\n",U)
print("Singular Values:\n",S)
print("V Transpose:\n",Vt)