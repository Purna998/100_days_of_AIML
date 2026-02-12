# Use Sympy to compute second-order derivatives (Hessian Matrix)
import sympy as sp
# Define the function
x=sp.Symbol('x')
f=x**3+3*x**2
# Compute first derivative
f_derivative=sp.diff(f,x)
print("First Derivative:",f_derivative)
# Compute Second derivative
s_derivative=sp.diff(f_derivative,x)
print("Second Derivative:",s_derivative)