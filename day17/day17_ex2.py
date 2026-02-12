# Partial Derivative and Vector of Partial Derivative(Gradient)
import sympy as sp

x,y=sp.symbols('x y')
f=x**2+y**2
grad_x=sp.diff(f,x)
grad_y=sp.diff(f,y)

print("Partial Derivatives:",grad_x,grad_y)
