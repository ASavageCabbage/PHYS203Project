# class handling interplay between water, salt, and saltwater
import logging
import numpy as np

from utils.phases import *
from utils.absolute import gibbs

class Subsystem:

    def __init__(self, water, salt):
        self.water = water
        self.salt = salt
        self.n_dissolved = 0 # number of moles of salt dissolved in water
        self.S_mixing = 0 # entropy change from mixing of saltwater
        self.H_mixing = 0 # enthalpy change from mixing saltwater
        self.update()

    # gets the total amount of heat that's flowed in/out of the system from mixing
    def get_heat(self):
        return self.H_mixing

    # add n moles of water to the system
    def add_water(self, n):
        self.water.add_moles(n)
        self.update()
    
    # add n moles of salt to the system
    def add_salt(self, n):
        self.salt.add_moles(n)
        self.update()

    # updates all quantities
    def update(self):
        self.update_saltwater()
        self.G = self.calc_G()

    # caculates the current total Gibbs energy of the subsystem
    def calc_G(self):
        H = self.water.H + self.salt.H + self.H_mixing
        S = self.water.S + self.salt.S + self.S_mixing
        return gibbs(H,S,self.water.T)
    
    # dissolves the maximum amount of salt in water as possible (or precipitates
    # salt out of the water if necessary). 
    def update_saltwater(self):
        if self.water.n == 0:
            self.precipitate(self.n_dissolved)
            return
        concentration = self.n_dissolved/self.water.n
        if concentration < MAX_C:
            to_dissolve = (MAX_C - concentration)*self.water.n
            self.dissolve(to_dissolve)
        elif concentration > MAX_C:
            to_precipitate = (concentration - MAX_C)*self.water.n
            self.precipitate(to_precipitate)
        else:
            pass # this line is 100% entirely necessary
    
    # dissolves n moles of salt, or all salt if n moles are not available
    # to be dissolved, automatically updates enthalpy and entropy of mixing
    def dissolve(self, n_salt):
        if n_salt > (self.salt.n - self.n_dissolved):
            n_salt = self.salt.n - self.n_dissolved
        self.n_dissolved += n_salt
        self.update_S_mixing()
        self.update_H_mixing()

    # precipitates n moles of salt, or all salt if n moles are not available
    # to be precipitated, automatically updates enthalpy and entropy of mixing
    def precipitate(self, n_salt):
        if n_salt > self.n_dissolved:
            n_salt = self.n_dissolved
        self.n_dissolved -= n_salt
        self.update_S_mixing()
        self.update_H_mixing()

    # updates the entropy of mixing of the salt dissolved in water
    # entropy of mixing assumes an ideal mixture (i.e. no interactions),
    # which is fairly inaccurate for salt in water
    # if we decided to go nuts, this has some data 
    # https://web.mit.edu/lienhard/www/Thermophysical_properties_of_seawater-DWT-16-354-2010.pdf
    def update_S_mixing(self):
        n = self.water.n + self.n_dissolved
        if n > 0:
            x = self.n_dissolved/n
            self.S_mixing = -n*R*(x*np.log(x) + (1-x)*np.log(1-x))

    # updates the total enthalpy of mixing of the salt dissolved in water
    # assumes constant enthalpy of mixing, which is again inaccurate
    # for higher salt concentrations
    def update_H_mixing(self):
        self.H_mixing = self.n_dissolved*H_sol
    