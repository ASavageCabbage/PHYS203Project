# ice phase
import numpy as np

from utils.phases import *
from utils.absolute import enthalpy, gibbs

# all quantities (H, S, G) should be measured as quantities of formation
# for STP conditions, tabulated in standard metric units
# the density of ice is assumed to be constant, and
# pressure is assumed to be constant and atmospheric
# heat capacities are assumed to be constant with respect to temperature
# salt is assumed to be dissolved entirely in liquid water, not ice
## TODO add function (or like derive it first) that does this
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=2

class Ice(Phase):

    # initializes ice to default STP conditions
    # then adjusts to the given temperature
    # takes number of moles of ice and temperature as input
    def __init__(self, n, T):
        super().__init__(n, T, initial_T=STP_T)
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure)
    def calc_c_molar(self):
        return find_nearest_value(self.T, ICE_CP_MOL)

    # calculates enthalpy of formation per mole as a function 
    # temperature, assumes constant pressure and density
    def calc_H_molar(self):
        delta_T = self.T - STP_T
        return ICE_HF - self.c_molar*delta_T

    # calculates molar entropy of formation as a function of temperature
    def calc_S_molar(self):
        return ICE_SR - self.c_molar*np.log(self.T/STP_T)

    # calculates current gibbs per mole of phase
    def calc_G_molar(self):
        return gibbs(self.H, self.T, self.S_molar)
