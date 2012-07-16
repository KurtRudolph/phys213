from sympy import *
N_A = avogadro_constant = 6.022 * 10.**23 
R = gas_constant = 8.314 

T_0 = 35. + 273.
n = 1.5
V_0 = 0.015 # m^3
V_f = 0.0015 # m^3

alpha = 5./2.

gamma = (alpha + 1)/ alpha

P_0 = n * R * T_0 / V_0

P_f = P_0 * V_0**gamma / V_f**gamma

# b)
print(P_f)

# c)
T_f = P_f * V_f / (n * R)
DeltaT = T_f - T_0
DeltaU = alpha * n * R * DeltaT

print(DeltaU)
