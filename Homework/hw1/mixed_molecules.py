from sympy import * 

Ar_quantity = 7500.
Ar_melecular_weight = 40.
N_2_quantity = 2500.
N_2_melecular_weight = 28.
KE_total = 5. * 10.**(-17)
k_B = 1.381 * 10.**(-23)

t = symbols('t')
print(solve(3./2. * Ar_quantity* k_B * t + 5./2. * N_2_quantity * k_B * t - KE_total, t))


