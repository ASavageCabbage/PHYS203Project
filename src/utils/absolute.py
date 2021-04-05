# General thermodynamic formulae that may be of use

import numpy as np
from scipy import constants

def U_ideal(f, n, T):
    return (f/2) * n * constants.R * T

def enthalpy(U, P, V):
    return U + PV

def helmholtz(U, S, T):
    return U - S*T

def gibbs(H, S, T):
    return H - S*T

def vapour_eqn(P0, L, T0, T1):
    '''
    Input units:
    P0     - any
    L      - Joules/mol
    T0, T1 - Kelvin
    '''
    return P0 * np.exp((L/constants.R) * (np.power(T1, -1) - np.power(T0, -1)))
