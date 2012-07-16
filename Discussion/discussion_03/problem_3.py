from sympy import *
from mpmath import *
N_A = avogadro_constant = 6.022 * 10.**23 
#R = gas_constant = 8.314 # J * K**(-1) * mol**(-1)
R = gas_constant = .082057 # L * atm * K**(-1) * mol**(-1)

Cu_density =  Cu_gamma = 8900 # Kg /m**3

Cu_specific_heat = Cu_c = 386 # J / kg -k

Cu_thermal_conductivity = Cu_kappa = 400 # W / m - k

Wire_length = Wire_l = .005 # m

Wire_diameter = Wire_d =  .001 # m
Wire_r = .5 * Wire_d

Wire_T_0 = 20. + 273.

Sodering_iron_T_0 = 250. + 273.

Wire_T_f = 200. + 273.

# 1)
Wire_mass = Cu_gamma * Wire_l * pi * Wire_r**2
print( Wire_mass)

# 2)
Wire_C = Wire_mass * Cu_c
print( Wire_C)


# 3)



