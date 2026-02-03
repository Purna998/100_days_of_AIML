# Write a program to generate a dataset of random floats and normalize the values between 0 and 1

import numpy as np
# arr=np.random.rand(1,51)
arr=np.random.uniform(low=1,high=51,size=5)
min_val=np.min(arr)
max_val=np.max(arr)
min_max_normalize= (arr-min_val)/(max_val-min_val)
print("Original Array: \n",arr)
print("Normalize Array from 0 to 1: \n",min_max_normalize)