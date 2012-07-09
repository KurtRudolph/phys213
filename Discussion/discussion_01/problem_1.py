from sympy import *

m_1 = 2.0
m_2 = 6.0

# momentume is m * v
# KE = \rho^ 2/2 * m

# a)

v = symbols( 'v')

rho_0 = ( 2.0 * m_1 *  16.0)**(1.0/2.0)



print( rho_0 )

# b)

rho_f = rho_0

print( rho_f)

# c)

ke = rho_f**2/( 2 * (m_1+ m_2))
print( ke)

# d)

print( "none")
