from sympy import *

N = 10**6

DeltaV = 0.0001 * V_0
V_f = V_0 + DeltaV

M_0 = n_T * V_0
M_f = n_T * V_f

M_0**N = (n_T * V_0)**N
M_f**N = (n_T * V_f)**N
