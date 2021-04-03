## salwater phase
## Last updated: 02/04/2021
## is python style to use getters and setters?

# there's got to be a more elegant way than this nonsense
from phase import Phase

# all quantities (U, S, G) should be measured as quantities of formation
# for STP conditions, tabulated in standard metric units
# the volume of water is assumed to be unaffected by dissolved salt
# pressure is assumed to be constant and atmospheric
# heat capacities have to be adjusted based on the salt concentration,
# and are assumed to be constant with respect to temperature
## TODO add function (or like derive it first) that does this
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=2

class Saltwater(Phase):
    
    p = 0 ## TODO update this, concentration of pure water in mol/m^3
    pure_U_molar = -285830 # enthalpy of formation of pure water
    pure_c_molar = 0 # TODO update this, molar heat capacity of pure water

    # initializes water to default STP conditions, no salt
    # takes number of moles of water as input
    def __init__(self, n):
        ## TODO Update this with proper values
        self.U_molar = pure_U_molar # energy per mole of water
        self.n_salt = 0 # number of moles of salt
        self.n_water = n
        self.c_molar = self.calc_c_molar()
        self.S_molar = 0 # TODO calculate this
        self.U = self.U_molar * self.n_water # internal energy
        self.S = self.S_molar * self.n_water # entropy
        self.T = 298 # temperature
        self.G_molar = self.calc_G_molar()
        self.G = G_molar * self.n_water # gibbs's free energy
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure) as a function of
    # salt concentration
    def calc_c_molar(self):
        pass

    # calculates internal energy per mole as a function of salt concentration
    # and temperature
    # TODO: Write this function
    def calc_U_molar(self):
        pass

    # calculates molar entropy as a function of salt concentration, temperature
    def calc_S_molar(self):
        pass

    # calculates current gibbs per mole of phase
    def calc_G_molar(self):
        return self.U_molar + P_ATM/p - self.T*self.S_molar

    # updates all molar quantities
    def update_molar(self):
        self.U_molar = self.calc_U_molar()
        self.S_molar = self.calc_S_molar()
        self.G_molar = self.calc_G_molar()

    ## Non-molar quantity functions

    # updates all non-molar quantities (except temperature, moles)
    def update_non_molar(self):
        self.U = self.U_molar * self.n_water
        self.S = self.S_molar * self.n_water
        self.G = self.G_molar * self.n_water

    # updates all quantities (except temperature, moles)
    def update(self):
        update_molar()

    ## System access functions

    # adds n moles of water to the phase object, this should handle updating
    # gibbs energy, entropy and internal energy itself
    def add_moles(self, n_water):
        self.n_water = n_water
        self.update()

    # adds/removes an amount of energy e from the system as heat, and updates
    # system accordingly
    def change_energy(self, e):
        self.T = e/(self.c_molar * n_water)
        self.update()

