# Differential forms of the Thermodynamic Identity
# Can be used for linear approximation

def dU(T, P, dS = 0, dV = 0):
    return T*dS - P*dV

def dH(T, V, mu, dS = 0, dP = 0, dN = 0):
    return T*dS + V*dP + mu*dN

def dF(S, P, mu, dT = 0, dV = 0, dN = 0):
    return 0 - S*dT - P*dV + mu*dN

def dG(S, V, mu, dT = 0, dP = 0, dN = 0):
    return 0 - SdT + V*dP + mu*dN
