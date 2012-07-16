from sympy import *
k = 1.38 * 10**(-23)
R = 8.314 
N_2_molar_mass = 28 # grams /mole

T_0 = 15. + 273.
T_f = 25. + 273.
DeltaT = T_f - T_0
P_0 = 1.04 * 10**5 # Pa
V = 2.8**3


#PV = n R T 
n = (P_0 * V) / (R * T_0)
P_f = n * R * T_f / (V)
DeltaU = 5./2. * V * ( P_f - P_0)

# 1)
print( DeltaU)

# 2)
print( DeltaU)

# 3)
C_V = DeltaU / DeltaT
print( C_V)

# 4)

print( P_f)
