# ndarray manipulation in numpy
import numpy as np
arr=np.array([1,2,3,4,5,6])

#reshaping to matrix seeing to no.of elements
reshaped=arr.reshape(2,3) # here are 6 elements so, we can make 3*2 or 2*3 matrix only
print(reshaped)

arr1=np.array([1,2,3])
expanded=arr1[:,np.newaxis]
print(expanded)