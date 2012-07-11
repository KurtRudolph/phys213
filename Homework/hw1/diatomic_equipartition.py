from sympy import * 

avogadros_number = 6.0221415 * 10**(23)
p = 2. * 101325. # pa pressue
mass_density = 1.7 / 1000. # kg per liter
attomic_weight = 28. / 1000. # kg per mole
k = 1.381 * 10**(-23) # I have no idea
R = 8.3144621 # gas constant


m = attomic_weight/avogadros_number

n = mass_density/m

T = p/( n * R)
KE = 3./2. * k * T

v = symbols( 'v')
print( solve( 1./2. * m * v**2 - KE, v))
