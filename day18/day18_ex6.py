# Use Adam Optimizer for a more complex dataset
# y=4+3*x+2*x**2+noise
import numpy as np

np.random.seed(42)

# Generate nonlinear data
m = 200
X = 2 * np.random.rand(m, 1) - 1
y = 4 + 3*X + 2*(X**2) + np.random.randn(m, 1)

# Create polynomial features [1, x, x^2]
X_poly = np.c_[np.ones((m,1)), X, X**2]

def adam_optimizer(X, y, theta, learning_rate=0.01, 
                   n_epochs=500, beta1=0.9, beta2=0.999, epsilon=1e-8):
    
    m = len(y)
    m_t = np.zeros_like(theta)  # First moment
    v_t = np.zeros_like(theta)  # Second moment
    
    for t in range(1, n_epochs + 1):
        
        # Compute gradient (Batch Gradient)
        gradients = 2/m * X.T @ (X @ theta - y)
        
        # Update biased first moment estimate
        m_t = beta1 * m_t + (1 - beta1) * gradients
        
        # Update biased second raw moment estimate
        v_t = beta2 * v_t + (1 - beta2) * (gradients**2)
        
        # Bias correction
        m_hat = m_t / (1 - beta1**t)
        v_hat = v_t / (1 - beta2**t)
        
        # Parameter update
        theta -= learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)
        
    return theta

# Initialize parameters
theta = np.random.randn(3,1)

# Train using Adam
theta_adam = adam_optimizer(X_poly, y, theta)

print("Optimized Parameters using Adam:\n", theta_adam)
