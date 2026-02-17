# Compute the expectation and variance of a weighted die(biased probabilities)

import numpy as np

# Die faces
faces = np.array([1,2,3,4,5,6])

# Biased probabilities
probabilities = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.25])

# Expectation
expectation = np.sum(faces * probabilities)

# E(X^2)
E_X2 = np.sum((faces**2) * probabilities)

# Variance
variance = E_X2 - expectation**2

print("Expectation:", expectation)
print("Variance:", variance)
