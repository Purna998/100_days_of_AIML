# Simple Bayes theorem implementation

def bayes_theorem(prior,likelihood,evidence):
    return (likelihood * prior) / evidence

prob=bayes_theorem(0.5,0.35,0.5)
print("Probability of A given on B: ",prob)