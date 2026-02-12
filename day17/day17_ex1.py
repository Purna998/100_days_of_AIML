 # Calculus: Derivatives- It measures the rate at which a f(x) changes with respect to it's input
import sympy as sp

x=sp.Symbol('x')
f=x**2
derivative=sp.diff(f)

print("Derivative:",derivative)