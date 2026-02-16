# Calculate Mean, Variance and standard deviation
import numpy as np

data=[10,20,30,40,50]

# Calulate stats
mean=np.mean(data)
variance=np.var(data)
std_dev=np.std(data)

print("Mean: ",mean)
print("Variance: ",variance)
print("Standard Deviation: ",std_dev)