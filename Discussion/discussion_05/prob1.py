from sympy import *
from math import *

k = 1.381 * 10**(-23)

d_E_C = 18.
d_E_B = 8.

E_C = -1.5
E_B = -3.4

T = 2000.

P_E_C = d_E_C * e**( -E_C / (k * T))
P_E_B = d_E_B * e

print( P_E_C / P_E_B)
