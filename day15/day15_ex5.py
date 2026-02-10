# Verify Properties of matrix multiplication
import numpy as np

# Non-Commutative: AB not equal to BA
A=np.array([[1,2],[3,4]])
B=np.array([[9,8],[7,6]])

matrix_multiply1=np.dot(A,B)
matrix_multiply2=np.dot(B,A)

if matrix_multiply1.all()==matrix_multiply2.all():
    print("AB is equal to BA")
else:
    print("AB is not equal to BA")

# Associative: A(BC) = (AB)C for matrices
C=np.array([[4,5],[8,7]])
matrix_multiply3=np.dot(B,C)
matrix_multiply4=np.dot(A,matrix_multiply3)
matrix_multiply5=np.dot(matrix_multiply1,C)

if matrix_multiply4.all()==matrix_multiply5.all():
    print("A(BC)=(AB)C")
else:
    print("A(BC) is not equal to (AB)C")


