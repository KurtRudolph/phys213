from sympy import * 

mol = 1.
J = Jouls = 1.
K = Kalvin = 1.

N_A = avogadro_constant = 6.022 * 10.**23 / mol
k = boltzmann_constant = 1.381 * 10.**(-23) / mol
R = gas_constant = 8.314 * J / mol * K 

kg = 1000

O_2_in_oxygen = .2
O_2_molar_mass = 31.99886
O_2_m = O_2_molar_mass / N_A
N_2_in_oxygen = .8
N_2_molar_mass =  28.01344

O_2_N_2_molar_mass = 60.01230
O_2_N_2_m = O_2_N_2_molar_mass / N_A
# 1)
print( O_2_in_oxygen)

#2)
T_0 = 22. + 273.
T_f = 52. + 273.

KE_0 = 3./2. * k * T_0
KE_f = 3./2. * k * T_f

Delta_KE = KE_f - KE_0
v = symbols('v')
v_0 = solve( .5 * O_2_N_2_m * v**2 - KE_0)[0]
v_f = solve( .5 * O_2_N_2_m * v**2 - KE_f)[0]

print( abs(v_f/v_0))

# c)

KE = symbols('KE')
KE_hat = solve( .5 * O_2_N_2_m * (2 * v_0)**2 - KE)[0]
T = symbols('T')
T_hat = solve( 3./2. * k * T - KE_hat)[0]

print( T_hat)


# d
P_0 = O_2_N_2_molar_mass * R * T_0
T_hat = solve( O_2_N_2_molar_mass * R * T - 2*P_0)[0]

print( T_hat)

# e
v_hat = 300
T_hat =  solve( 3./2. * k * T - (.5 * O_2_m / kg * (v_hat)**2))[0]

print( T_hat)
