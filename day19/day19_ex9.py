import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform

# create x range
x = np.linspace(-4, 4, 1000)  # min=-4 and max=4

# Normal Distribution (mean=0, std=1)
gaussian = norm.pdf(x, loc=0, scale=1)

# Uniform Distribution (between min=-2 and max=2)
uniform_dist = uniform.pdf(x, loc=-2, scale=4)

# plot
plt.plot(x, gaussian, label="Gaussian (Normal)")
plt.plot(x, uniform_dist, label="Uniform")

plt.title("Gaussian vs Uniform Distribution")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
