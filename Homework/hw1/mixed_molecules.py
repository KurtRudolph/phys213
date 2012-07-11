from sympy import * 

t_0 = symbols('t_0')
print( solve( 1.0 - 1.0/30.0 * t_0 + t_0/60.0**2 - 1.0/2.0, t_0))
