# class handling the interplay of different distinct phases in a system
# and the resivoir

from utils.phases import *
from utils.subsystem import Subsystem

class System:

    def __init__(self, n_salt, n_water, n_ice, T):
        salt = Salt(n_salt, T)
        water = Water(n_water, T)
        self.ice = Ice(n_ice, T)
        self.subsystem = Subsystem(water, salt)
        self.T = T
    
    # calculates the total Gibbs energy of the system
    def calc_G(self):
        return self.ice.G + self.subsystem.G

    # moves n particles of ice to water, or n particles of water
    # to ice if n is negative.
    def move_ice(self, n):
        if self.ice.n < n: # deal with cases of not enough moles being
            n = self.ice.n # available to move
        elif self.subsystem.water.n < (-n):
            n = -self.subsystem.water.n
        self.ice.add_moles(-n)
        self.subsystem.add_water(n)
