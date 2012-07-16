from sympy import * 

mol = 1.
J = Jouls = 1.

K = Kalvin = 1.
c = celcius = K - 273.

L = liter = 1.

kg = kilogram = 1000.
g = gram = 1. / kg

pa = 1.
atm = 9.8692 * 10**(-6) * pa

N_A = avogadro_constant = 6.022 * 10.**23 / mol
k = boltzmann_constant = 1.381 * 10.**(-23) / mol
R = gas_constant = 8.314 * J / mol * K 

N_2_molar_mass =  28.01344 * g / mol

# Let
m = N_2_mass_density = 1.7 * g / L
P = pressure = 2. * atm 
V = volume = 1. * L

N = amount_of_substance = N_2_mass_density * V / N_2_molar_mass * N_A

T = P * V / (N * k)
KE = 3./2. * k * T

v = symbols( 'v')
print( solve( 1./2. * m * v**2 - KE, v))
