# Generate a random array and find the minimum and maximum values
import numpy as np
# import random
# arr=[]
# for i in range(10):
#     random_value=random.randrange(100)
#     arr.append(random_value)
# print(arr)

rng=np.random.default_rng()
arr=rng.random(size=8)
print("The Minimum is: ",arr.min())
print("The Maximum is: ",arr.max())
print(arr)