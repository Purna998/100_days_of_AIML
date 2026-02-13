# Visualize the loss function's surface and the SGD optimization path
import numpy as np
import matplotlib.pyplot as plt

# Loss function
def loss(w1, w2):
    return w1**2 + w2**2

# Gradient
def grad(w1, w2):
    return 2*w1, 2*w2

# Simple SGD
w1, w2 = 4, 4
lr = 0.2
path_w1 = [w1]
path_w2 = [w2]

for i in range(15):
    dw1, dw2 = grad(w1, w2)
    w1 = w1 - lr * dw1
    w2 = w2 - lr * dw2
    path_w1.append(w1)
    path_w2.append(w2)

# Create surface
w1_vals = np.linspace(-5, 5, 100)
w2_vals = np.linspace(-5, 5, 100)
W1, W2 = np.meshgrid(w1_vals, w2_vals)
Z = loss(W1, W2)

# Contour plot
plt.contour(W1, W2, Z, 30)
plt.plot(path_w1, path_w2, marker='o')
plt.xlabel("w1")
plt.ylabel("w2")
plt.title("Loss Surface and SGD Path")
plt.show()
