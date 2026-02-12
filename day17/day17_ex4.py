# Compute Gradiants

import sympy as sp

# Define a multivariable function
x,y=sp.symbols('x y')
f=x**2+3*y**2-4*x*y

# Compute Partial derivative
gradient_x=sp.diff(f,x)
gradient_y=sp.diff(f,y)

print("Gradients:")
print("Gradient X:",gradient_x)
print("Gradient_y:",gradient_y)
