# Create a 3D random array and compute statistics along specific axes

import numpy as np
# Generate a random 3d array
arr=np.random.randint(1,51,size=(3,3))
print("Original: \n",arr)

# Compute rows and columns stat
row_sum=np.sum(arr,axis=1)
print("Row Sum: \n",row_sum)

column_sum=np.sum(arr,axis=0)
print("Column Sum: \n",column_sum)

row_mean=np.mean(arr,axis=1)
print("Row Mean: \n",row_mean)

column_mean=np.mean(arr,axis=0)
print("Column Mean: \n",column_mean)

row_std=np.std(arr,axis=1)
print("Row STD: \n",row_std)

column_std=np.std(arr,axis=0)
print("Column STD: \n",column_std)


