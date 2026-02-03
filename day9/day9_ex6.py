# Generate and Filter a Random Dataset

import numpy as np

# Generate a random Dataset
dataset=np.random.randint(1,51,size=(5,5))
print("Original: \n",dataset)

# Filter values >25 and replace with 0
dataset[dataset>25]=0
print("Modified Dataset: \n",dataset)

# Calculate summary stats
print("Sum: \n",np.sum(dataset))
print("Mean: \n",np.mean(dataset))
print("Standard Deviation: \n",np.std(dataset))


