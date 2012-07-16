from sympy import *
N_A = avogadro_constant = 6.022 * 10.**23 
#R = gas_constant = 8.314 # J * K**(-1) * mol**(-1)
R = gas_constant = .082057 # L * atm * K**(-1) * mol**(-1)

alpha = 5./2.
gamma = (alpha + 1) / alpha

T_0 = 300 # K
P_0 = 1 # atm
V_0 = 1 # L

V_e = 2 # L

V_f = 1 # L

n = P_0 * V_0 / (R * T_0)

P_e = P_0 * V_0**gamma / V_e**gamma 

T_e = P_e * V_e / (n * R)

DeltaT = T_e - T_0

DeltaU = alpha * n * R * DeltaT
