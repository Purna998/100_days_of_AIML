# Write a program to normalize an array (scale values between 0 and 1)
import numpy as np

# Scratch normalization using Min-Max
def min_max_normalize(arr):
    arr=arr.astype(float)
    minimum=arr.min()
    maximum=arr.max()

    if minimum==maximum:
        return arr
    arr_normalize=(arr-minimum)/(maximum-minimum)
    return arr_normalize

arr=np.array([20,13,56,34,98,121])
normalized_data=min_max_normalize(arr)
print(normalized_data)

# using Scikit Learn
from sklearn.preprocessing import minmax_scale
normalize=minmax_scale(arr)
print(normalize)