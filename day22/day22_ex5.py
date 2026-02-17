# Simulate flipping a coin 10,000 times and calculate probabilities of heads/tails

import numpy as np

flips=np.random.randint(1,3,size=10000)
print(flips)
probability_heads=np.sum(flips==1)/len(flips)
probability_tails=np.sum(flips==2)/len(flips)
print(probability_heads)
print(probability_tails)
