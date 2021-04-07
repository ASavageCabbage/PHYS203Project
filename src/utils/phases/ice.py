# ice phase

import logging
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
        self.n_ice = n
        self.T = STP_T
        self.update()
        self.add_heat(self.c_molar*self.n_ice*(T - STP_T)) # cool system
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure)
    # TODO: Check the usage of find_nearest_value is correct
    def calc_c_molar(self):
        return find_nearest_value(self.T, ICE_CP)

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

    # updates all molar quantities
    def update_molar(self):
        self.c_molar = self.calc_c_molar()
        self.H_molar = self.calc_H_molar()
        self.S_molar = self.calc_S_molar()
        self.G_molar = self.calc_G_molar()
        logging.debug(
            "Updated molar values:\n"
         + f"Cp = {self.c_molar}, H = {self.H_molar}, S = {self.S_molar}, G = {self.G_molar}"
        )

    ## Non-molar quantity functions

    # updates all non-molar quantities (except temperature, moles)
    def update_non_molar(self):
        self.H = self.H_molar * self.n_ice
        self.S = self.S_molar * self.n_ice
        self.G = self.G_molar * self.n_ice
        logging.debug(
            "Updated non-molar values:\n"
         + f"H = {self.H}, S = {self.S}, G = {self.G}"
        )

    # updates everything
    def update(self):
        self.update_molar()
        self.update_non_molar()

    ## System access functions

    # adds n moles of ice to the phase object, this should handle updating
    # gibbs energy, entropy and internal energy itself
    def add_moles(self, n_ice):
        self.n_ice = n_ice
        self.update()

    # adds/removes an amount of energy e from the system as heat, and updates
    # system accordingly
    def add_heat(self, e):
        self.T = e/(self.c_molar * n_ice)
        self.update()