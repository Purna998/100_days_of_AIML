# Random Number Generation and setting seeds
# Random Number Generation - np.random

import numpy as np

#Setting Random seeds
np.random.seed(42) # If one time random work and generate random numbers then, seed ensure to not to change

random_array=np.random.rand(3,3)
print("Random Array: \n",random_array)    

random_integers=np.random.randint(0,10,size=(2,3))
print("Random Integers: \n", random_integers)   #[[7 2 5]
                                                #[4 1 7]]


