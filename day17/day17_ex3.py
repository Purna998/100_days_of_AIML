# Compute Derivatives of Basic Functions

import sympy as sp

x=sp.Symbol('x')
f=x**3-5*x-8
derivative= sp.diff(f,x)
print("Function:",f)
print("Derivative:",derivative)
