from sympy import *

m_A = 360
m_B = 1000
T_A = 200 + 273.15
T_B = 27 + 273.15
c_B = 452
Beta = .64
T_f = symbols('T_f')
T_f = solve( (.5 * m_A * Beta) * T_f**2 + (m_B * c_B) * T_f + ( -.5 * m_A * Beta * T_A**2 - m_B * c_B * T_B), T_f)[0]

DeltaS_BlockB = m_B * c_B * log( T_f / T_B)
DeltaS_BlockA = m_A * 0.64 * (T_f - T_A)
DeltaS = DeltaS_BlockA + DeltaS_BlockB
print( DeltaS)