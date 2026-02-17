# Explore other distributions (e.g. normal, ninomial ) using python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom

# Normal Distribution (Continuous)
# Parameters
mu = 0
sigma = 1

# Generate x values
x_normal = np.linspace(-4, 4, 200)

# PDF
pdf_normal = norm.pdf(x_normal, mu, sigma)

plt.figure()
plt.plot(x_normal, pdf_normal)
plt.title("PDF of Normal Distribution (μ=0, σ=1)")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.show()

print("Normal Distribution")
print("Mean:", norm.mean(mu, sigma))
print("Variance:", norm.var(mu, sigma))

# Binomial Distribution (Discrete)
# Parameters
n = 10
p = 0.5

# Possible outcomes
x_binomial = np.arange(0, n+1)

# PMF
pmf_binomial = binom.pmf(x_binomial, n, p)

plt.figure()
plt.bar(x_binomial, pmf_binomial)
plt.title("PMF of Binomial Distribution (n=10, p=0.5)")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show()

print("\nBinomial Distribution")
print("Mean:", binom.mean(n, p))
print("Variance:", binom.var(n, p))
