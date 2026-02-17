from itertools import product

# Sample space of a dice
sample_spce=list(range(1,7))

# Pobability of rolling an even number
even=[2,4,6]
p_even=len(even)/len(sample_spce)
print("P(Even): ",p_even)