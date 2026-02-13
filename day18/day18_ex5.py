# Implement mini-batch SGD and compare it with vanilla SGD
import numpy as np

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add bias term
X_b = np.c_[np.ones((100,1)), X]

def mini_batch_sgd(X, y, theta, learning_rate, n_epochs, batch_size):
    m = len(y)
    for epoch in range(n_epochs):
        indices = np.random.permutation(m)
        X_shuffled = X[indices]
        y_shuffled = y[indices]
        
        for i in range(0, m, batch_size):
            xi = X_shuffled[i:i+batch_size]
            yi = y_shuffled[i:i+batch_size]
            
            gradients = 2/batch_size * xi.T @ (xi @ theta - yi)
            theta -= learning_rate * gradients
    return theta

#Initialize parameters
theta=np.random.randn(2,1)
learning_rate=0.01
n_epochs=50
batch_size=100000

# Perform SGD
theta_optimize=mini_batch_sgd(X_b,y,theta,learning_rate,n_epochs,batch_size)
print("Optimized Parameters:",theta_optimize)