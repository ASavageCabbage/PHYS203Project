## parent (abstract) class for a phase
## Last updated: 31/03/2021
## is python style to use getters and setters?

class Phase:

    p = 0 # density (mol/m^3)
    c = 0 # heat capacity at constant pressure (J/K)
    
    def __init__(self, V_0, T_0):
        # all quantities (U, S, G) should be with respect to the same reference point
        # all should also be measured using standard SI units
        # density is intrinsic to the particular phase, pressure is assumed to be
        # constant (and atmospheric for now)
        # system is assumed to be in equilibrium with itself at all times
        self.U_molar = 0
        self.S_molar = get_S_molar(T_0)
        self.G_molar = get_G_molar(T_0)
        self.U = U_molar * (V_0*D) # internal energy
        self.V = V_0 # volume
        self.S = S_molar * (V_0*D) # entropy
        self.T = T_0 # temperature
        self.G = G_molar * (V_0*D) # gibbs's free energy
    
    ## Molar quantity functions

    # retuns molar entropy of the phase as a function of temperature
    def get_S_molar(T):
        pass

    # returns gibbs per mole as a function of temperature
    def get_G_molar(T):
        pass

    ## System access functions

    # returs the change in gibbs energy that results from adding one mole
    # of phase
    def test_add():
        pass

    # adds n moles of phase to the phase object, this should handle updating
    # gibbs energy and internal energy itself
    def add_moles(n):
        self.volume += n/p
        ## TODO add updating gibbs, energy, etc.

    # adds/removes an amount of energy e from the system as heat, and updates
    # temperature accordingly
    def change_energy(e):
        self.T += e/c
        ## TODO add updating gibbs, energy, etc.

    
    


    

        