# Simulate random variables from custom distributions
import numpy as np
import matplotlib.pyplot as plt

# Generate uniform samples
u=np.random.uniform(0,1, size=10000)
#Apply inverse transform of f(x)=x**2
x=np.sqrt(u)

plt.hist(x,bins=50,density=True)
plt.title("Custom Distribution using Inverse Transform")
plt.show()

# Using custom distribution class of scipy
from scipy.stats import rv_continuous

class custom_distribution(rv_continuous):
    def _pdf(self,x):
        if 0<=x<=1:
            return 3*x**2 
        else:
            return 0
dist=custom_distribution(a=0,b=1)
samples=dist.rvs(size=10000)
print(samples)
plt.hist(samples,bins=50,density=True)
plt.title("Custom Distribution using rv_continuous class")
plt.show()