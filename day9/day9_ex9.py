# Implement conditional replacement to create a binary mask for values above a threshold

import numpy as np

dataset=np.random.randint(1,51,size=14)
print(dataset)

mask=(dataset>34).astype(int)
print("Binary Masking: \n", mask)