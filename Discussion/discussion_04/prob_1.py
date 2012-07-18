from sympy import *

# a)
num_spins = 7

Omega = total_num_micro_states = 2**num_spins

# b)
num_spins! / (num_spins_up! * num_spins_up!)

# c)

(num_spins! / (num_spins_up! * num_spins_up!)) / total_num_micro_states


sigma = log_e( Omega)
