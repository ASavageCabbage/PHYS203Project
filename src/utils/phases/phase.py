import logging

from utils.phases import *

# parent (abstract) class for a phase
#
# this still needs to be finished, I just wanted to move
# on to making an implementation to get a better idea of
# what's going on here
# THIS IS ONLY INTENDED TO SPECIFY WHAT SYSTEM ACCESS FUNCTIONS
# ARE NEEDED, NOTHING ELSE

class Phase:

    # initializes to default SATP conditions
    # then adjusts to the given temperature
    def __init__(self, n, T, initial_T=SATP_T):
        self.n = 0
        self.T = initial_T
        self.add_moles(n)
        self.add_heat(self.c_molar*self.n*(T - initial_T))

    # updates all quantities
    def update(self):
        self.c_molar = self.calc_c_molar()

        self.H_molar = self.calc_H_molar()
        self.H = self.H_molar * self.n

        self.S_molar = self.calc_S_molar()
        self.S = self.S_molar * self.n

        self.G_molar = self.calc_G_molar()
        self.G = self.G_molar * self.n

        logging.debug(
            "Updated molar values:\n"
         + f"Cp = {self.c_molar}, H = {self.H_molar}, S = {self.S_molar}, G = {self.G_molar}"
        )
        logging.debug(
            "Updated non-molar values:\n"
         + f"H = {self.H}, S = {self.S}, G = {self.G}"
        )
        
    ## System access functions

    # adds n moles of phase to the phase object, this should handle updating
    # gibbs energy and internal energy itself, returns how many moles were
    # added
    def add_moles(self, n):
        self.n += n
        if self.n < 0:
            self.n = 0
        self.update()

    # adds/removes an amount of energy e from the system as heat, and updates
    # temperature accordingly
    def add_heat(self, e):
        if self.n > 0:
            self.T += e/(self.c_molar * self.n)
        self.update()
    
    ## Unimplemented functions (must be implemented by concrete class)
    def calc_c_molar(self): raise NotImplementedError()
    def calc_H_molar(self): raise NotImplementedError()
    def calc_S_molar(self): raise NotImplementedError()
    def calc_G_molar(self): raise NotImplementedError()
