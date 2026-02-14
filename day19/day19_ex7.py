# Plot and Explore Different Probability Distributions

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm,binom,poisson

# Gaussian Normal Distribution
x1=np.linspace(-4,4,100)
y1=norm.pdf(x1,loc=0,scale=1) # pdf=probability density function

plt.plot(x1,y1,label="Gaussian")
plt.title("Gaussian Normal Distribution")
plt.show()

# Binomial Distributions
n,p=10,0.5
x2=np.arange(0,n+1)
y2=binom.pmf(x2,n,p)
plt.bar(x2,y2,label="Binomial")
plt.title("Binomial Distribution")
plt.show()

# Poisson Distribution
lam=3
x3=np.arange(0,10)
y3=poisson.pmf(x3,lam)
plt.bar(x3,y3,label="Poisson")
plt.title("Poisson Distribution")
plt.show()