import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multinomial

# total trials
n = 10

# probabilities for 3 classes
p = [0.2, 0.5, 0.3]

# possible outcomes (must sum to 10)
x = np.array([
    [2,5,3],
    [3,4,3],
    [1,6,3],
    [0,7,3],
    [4,3,3]
])

# compute pmf directly
y = multinomial.pmf(x, n, p)

# plot
plt.bar(range(len(x)), y)
plt.title("Multinomial Distribution")
plt.xlabel("Outcome Combinations")
plt.ylabel("Probability")
plt.xticks(range(len(x)), x, rotation=45)
plt.show()
