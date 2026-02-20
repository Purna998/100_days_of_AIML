# Visualize confidence intervals for multiple samples using Matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Simulate 5 samples
np.random.seed(42)
samples = [np.random.normal(loc=mu, scale=5, size=20) for mu in [50, 55, 60, 65, 70]]
# Prepare lists for means and CIs
means = []
lower = []
upper = []
# Compute mean and 95% CI for each sample
confidence = 0.95
for sample in samples:
    n = len(sample)
    mean = np.mean(sample)
    sem = np.std(sample, ddof=1) / np.sqrt(n)
    h = sem * t.ppf((1 + confidence) / 2, n - 1)
    
    means.append(mean)
    lower.append(mean - h)
    upper.append(mean + h)

# Plot
x = np.arange(1, len(samples)+1)
plt.errorbar(x, means, yerr=[np.array(means)-np.array(lower), np.array(upper)-np.array(means)],
             fmt='o', capsize=5, capthick=2)
plt.xticks(x)
plt.xlabel("Sample Number")
plt.ylabel("Mean ± 95% CI")
plt.title("Confidence Intervals for Multiple Samples")
plt.show()
