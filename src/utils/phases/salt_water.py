# saltwater phase

import logging
import numpy as np

from utils.phases import *
from utils.absolute import enthalpy, gibbs

# all quantities (H, S, G) should be measured as quantities of formation
# for SATP conditions, tabulated in standard metric units
# the volume of water is assumed to be unaffected by dissolved salt
# pressure is assumed to be constant and atmospheric
# heat capacities have to be adjusted based on the salt concentration,
# and are assumed to be constant with respect to temperature
## TODO add function (or like derive it first) that does this
# https://webbook.nist.gov/cgi/cbook.cgi?ID=C7732185&Mask=2

class Saltwater(Phase):

    # initializes water to default SATP conditions, no salt
    # then adjusts to the given temperature
    # takes number of moles of water and temperature as input
    def __init__(self, n, T):
        self.n_salt = 0 # number of moles of salt
        super().__init__(n, T)
    
    ## Molar quantity functions

    # calculates molar heat capacity (at constant pressure)
    # with the current salt concentration
    def calc_c_molar(self):
        molarity = self.n_salt / self.n
        relative_cp = find_nearest_value(molarity, NACL_MOLAR_RELATIVE_CP)
        pure_cp = LIQUID_WATER_CP
        return relative_cp * pure_cp

    # calculates enthalpy of formatino per mole as a function of salt concentration
    # and temperature, assumes constant pressure and density
    def calc_H_molar(self):
        satp_H = LIQUID_WATER_HF + SALT_HF + (self.n_salt/self.n)*SALT_SOLUTION_H
        delta_T = self.T - SATP_T
        return satp_H - self.c_molar*delta_T

    # calculates molar entropy of formation as a function of salt concentration, temperature
    def calc_S_molar(self):
        S_satp = LIQUID_WATER_SR + (self.n_salt/self.n)*SOLID_SALT_SR
        return S_satp - self.c_molar*np.log(self.T/SATP_T)

    # calculates current gibbs per mole of phase
    def calc_G_molar(self):
        return gibbs(self.H, self.T, self.S_molar)

    # adds n moles of salt to the water, updates heat capacity, Gibbs energy,
    # and entropy, and returns how much heat was released during dissolution
    def add_salt(self, n_salt):
        self.n_salt += n_salt
        self.update()
        return -1*n_salt*SALT_SOLUTION_H
