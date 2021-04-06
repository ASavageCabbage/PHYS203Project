# saltwater phase

import logging
import numpy as np

from utils.phases import *
from utils.absolute import enthalpy, gibbs

# all quantities (U, S, G) should be measured as quantities of formation
# for STP conditions, tabulated in standard metric units
# the volume of water is assumed to be unaffected by dissolved salt
# pressure is assumed to be constant and atmospheric
# heat capacities have to be adjusted based on the salt concentration,
# and are assumed to be constant with respect to temperature
## TODO add function (or like derive it first) that does this
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=2
## NOTE: stuff only works for liquid water rn

class Saltwater(Phase):

    # initializes water to default STP conditions, no salt
    # takes number of moles of water as input
    def __init__(self, n):
        self.n_salt = 0 # number of moles of salt
        self.n_water = n
        self.T = STP_T
        self.update()
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure)
    # with the current salt concentration
    def calc_c_molar(self):
        molarity = self.n_salt / self.n_water
        relative_cp = find_nearest_value(molarity, NACL_MOLAR_RELATIVE_CP)
        pure_cp = find_nearest_value(self.T, LIQUID_WATER_CP)
        return relative_cp * pure_cp

    # calculates internal energy per mole as a function of salt concentration
    # and temperature
    def calc_U_molar(self):
        stp_U = LIQUID_WATER_HF - STP_P/LIQUID_WATER_MOLAR_CONC
        delta_T = self.T - STP_T
        return stp_U - self.c_molar*delta_T

    # calculates molar entropy as a function of salt concentration, temperature
    def calc_S_molar(self):
        return LIQUID_WATER_S - self.c_molar*np.log(self.T/STP_T)

    # calculates current gibbs per mole of phase
    def calc_G_molar(self):
        H = enthalpy(self.U_molar, STP_P, 1/LIQUID_WATER_MOLAR_CONC)
        return gibbs(H, self.T, self.S_molar)

    # updates all molar quantities
    def update_molar(self):
        self.c_molar = self.calc_c_molar()
        self.U_molar = self.calc_U_molar()
        self.S_molar = self.calc_S_molar()
        self.G_molar = self.calc_G_molar()
        logging.debug(
            "Updated molar values:\n"
         + f"Cp = {self.c_molar}, U = {self.U_molar}, S = {self.S_molar}, G = {self.G_molar}"
        )

    ## Non-molar quantity functions

    # updates all non-molar quantities (except temperature, moles)
    def update_non_molar(self):
        self.U = self.U_molar * self.n_water
        self.S = self.S_molar * self.n_water
        self.G = self.G_molar * self.n_water
        logging.debug(
            "Updated non-molar values:\n"
         + f"U = {self.U}, S = {self.S}, G = {self.G}"
        )

    # updates everything
    def update(self):
        self.update_molar()
        self.update_non_molar()

    ## System access functions

    # adds n moles of water to the phase object, this should handle updating
    # gibbs energy, entropy and internal energy itself
    def add_moles(self, n_water):
        self.n_water = n_water
        self.update()

    # adds/removes an amount of energy e from the system as heat, and updates
    # system accordingly
    def add_heat(self, e):
        self.T = e/(self.c_molar * n_water)
        self.update()

