# Calculate Probabilities using Bayes' theorem

# Problem
# - A disease affects 1% of a population
# - A test is 95% for diseased individuals and 98% accurate for non-diseased individuals and 90% accurate for non-diseased individual
# - Find the probability of having the disease given a positive test result

def bayes_theorem(prior,sensitivity,specificity):
    evidence=(sensitivity*prior) +((1-specificity)*(1-prior))
    posterior=(sensitivity*prior)/evidence
    return posterior
prior=0.01 # 1% prevalence
sensitivity=0.95 # True Positive Rate
specificity=0.90 # True Negative Rate

posterior=bayes_theorem(prior,sensitivity,specificity)
print("Probability of Disease Given Positive Test:",posterior)
