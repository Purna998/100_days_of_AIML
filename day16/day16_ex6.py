# Verify the property of eigenvalues: det(A-lamda*I=0)

import numpy as np

# Creating matrix
A=np.array([[1,2],[3,4]])

#creaing 2*2 identity matrix
I=np.eye(2)

#finding eigenvalue
eigenval,eigenvec=np.linalg.eig(A) # lambda=eigenval

# Find complete determinant(det(A-eigenval*I) should 0)
for lam in eigenval:
    det=np.linalg.det(A-lam*I)
    print(f"lambda={lam}, det(A - λI) = {det}") # as property says determinant should 0



