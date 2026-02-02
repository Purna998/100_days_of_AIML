# Practice: 
# Create a 4*4 Matrix and calculate the sum of its rows and columns
import numpy as np
matrix=np.array([
    [1,2,3],
    [5,6,7],
    [9,8,3],
    [6,3,4]
])

# sum of row elements
row_sum=np.sum(matrix,axis=0)
print(row_sum)

# sum of columns elements
column_sum=np.sum(matrix,axis=1)
print(column_sum)