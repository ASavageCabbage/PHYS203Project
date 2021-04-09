# water phase
import numpy as np

from utils.phases import *
from utils.absolute import gibbs

# all quantities (H, S, G) should be measured as quantities of formation
# for SATP conditions, tabulated in standard metric units
# the volume of water is assumed to be unaffected by dissolved salt
# pressure is assumed to be constant and atmospheric
# heat capacities have to be adjusted based on the salt concentration,
# and are assumed to be constant with respect to temperature
## TODO add function (or like derive it first) that does this
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=2

class Water(Phase):

    # initializes water to default SATP conditions
    # then adjusts to the given temperature
    # takes number of moles of water and temperature as input
    def __init__(self, n, T):
        super().__init__(n, T)
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure)
    # with the current salt concentration
    def calc_c_molar(self):
        return LIQUID_WATER_CP

    # calculates enthalpy of formation per mole as a function of temperature
    # assumes constant pressure and density
    def calc_H_molar(self):
        delta_T = self.T - SATP_T
        return LIQUID_WATER_HF - self.c_molar*delta_T

    # calculates molar entropy of formation as a function of temperature
    def calc_S_molar(self):
        return LIQUID_WATER_SR - self.c_molar*np.log(self.T/SATP_T)

    # calculates current gibbs per mole of phase
    def calc_G_molar(self):
        return gibbs(self.H, self.T, self.S_molar)
