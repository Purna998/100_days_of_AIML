# Use Probability distributions to simulate and analyze real-world datasets
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, uniform, poisson, binom, multinomial

# Load dataset
df = pd.read_csv("sales_data.csv")

# 1️ NORMAL DISTRIBUTION (Sales_Amount)
sales = df["Sales_Amount"]
mu = sales.mean()
sigma = sales.std()

x = np.linspace(sales.min(), sales.max(), 1000)
normal_pdf = norm.pdf(x, mu, sigma)

plt.figure()
plt.hist(sales, bins=30, density=True, alpha=0.6)
plt.plot(x, normal_pdf)
plt.title("Normal Distribution Fit - Sales Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Density")
plt.show()

# 2️ UNIFORM DISTRIBUTION (Sales_Amount)

a = sales.min()
b = sales.max()
uniform_pdf = uniform.pdf(x, loc=a, scale=b-a)

plt.figure()
plt.hist(sales, bins=30, density=True, alpha=0.6)
plt.plot(x, uniform_pdf)
plt.title("Uniform Distribution - Sales Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Density")
plt.show()

# 3️ POISSON DISTRIBUTION (Quantity_Sold)

quantity = df["Quantity_Sold"]
lam = quantity.mean()
k = np.arange(0, quantity.max()+1)
poisson_pmf = poisson.pmf(k, lam)

plt.figure()
plt.hist(quantity, bins=range(int(quantity.max())+2), density=True, alpha=0.6)
plt.plot(k, poisson_pmf, marker='o')
plt.title("Poisson Distribution - Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Probability")
plt.show()

# 4️ BINOMIAL DISTRIBUTION (High Sales Event)
# Define success = Sales above median
success = (sales > sales.median()).astype(int)
n = len(success)
p = success.mean()
k = np.arange(0, n+1)
binom_pmf = binom.pmf(k, n, p)

plt.figure()
plt.plot(k, binom_pmf)
plt.title("Binomial Distribution - High Sales Event")
plt.xlabel("Number of High Sales")
plt.ylabel("Probability")
plt.show()

# 5️ MULTINOMIAL DISTRIBUTION (Product Category)

category_counts = df["Product_Category"].value_counts()
n_mult = category_counts.sum()
p_mult = category_counts / n_mult
observed_counts = category_counts.values
mult_prob = multinomial.pmf(observed_counts, n=n_mult, p=p_mult)

print("Multinomial Probability of Observed Category Counts:")
print(mult_prob)
