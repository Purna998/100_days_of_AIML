# Implement Gradient descent with multiple learning rates and compare convergence speeds

import numpy as np
import matplotlib.pyplot as plt

# Cost Function (Mean Squared Error)
# def compute_cost(X, y, theta):
#     m = len(y)
#     predictions = np.dot(X, theta)
#     errors = predictions - y
#     cost = (1/(2*m)) * np.sum(errors**2)
#     return cost

# Gradient Descent Function (returns theta + cost history)
def gradient_descent(X, y, theta, learning_rate, iterations):
    m = len(y)
    # cost_history = []
    
    for _ in range(iterations):
        predictions = np.dot(X, theta)
        errors = predictions - y
        gradients = (1/m) * np.dot(X.T, errors)
        theta = theta - learning_rate * gradients
        
        # cost = compute_cost(X, y, theta)
        # cost_history.append(cost)
        
    return theta # cost_history

# Sample Data
X = np.array([[1,1],[1,2],[1,3]])
y = np.array([2,2.5,3.5])
iterations = 100

# Different learning rates
learning_rates = [0.01, 0.1, 0.5]

# plt.figure()

for lr in learning_rates:
    theta = np.array([0.1, 0.1])
    optimized_theta = gradient_descent(X, y, theta, lr, iterations)
    
    # plt.plot(range(iterations), cost_history, label=f"LR = {lr}")
    print(f"Learning Rate {lr} → Final Theta: {optimized_theta}")

# plt.xlabel("Iterations")
# plt.ylabel("Cost")
# plt.title("Convergence Comparison for Different Learning Rates")
# plt.legend()
# plt.show()
