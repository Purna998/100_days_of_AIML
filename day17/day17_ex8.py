# visualize the gradient descent process on a quadratic function
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define symbolic variable
x = sp.Symbol('x')

# Define quadratic function
f_sym = x**2 + 4*x + 4

# Compute derivative symbolically
df_sym = sp.diff(f_sym, x)

print("Function f(x):", f_sym)
print("Derivative f'(x):", df_sym)

# Convert symbolic expressions to numerical functions
f = sp.lambdify(x, f_sym, "numpy")
df = sp.lambdify(x, df_sym, "numpy")

# Gradient Descent
def gradient_descent(start_x, learning_rate, iterations):
    x_val = start_x
    history = [x_val]
    
    for _ in range(iterations):
        x_val = x_val - learning_rate * df(x_val)
        history.append(x_val)
    
    return history

# Parameters
start_x = 8
learning_rate = 0.1
iterations = 10

# Run gradient descent
x_values = gradient_descent(start_x, learning_rate, iterations)

# Plot function
x_range = np.linspace(-10, 5, 400)
plt.plot(x_range, f(x_range))
plt.scatter(x_values, f(np.array(x_values)))
plt.title("Gradient Descent on Quadratic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()
