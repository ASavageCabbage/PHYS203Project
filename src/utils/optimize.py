# methods used to optimize (minimze) the Gibbs energy of the system
# TODO: Add a way to handle equilibrium, right now it's a bit random

import logging
import numpy as np
from scipy.optimize import minimize_scalar
from copy import deepcopy

from utils.system import System

class Optimizer:

    # constructs and returns minimizng function for particular system
    def minimze_Gibbs_func(system):
        
        toy_system = deepcopy(system)

        # function that returns the Gibbs energy for a particular system,
        # as a function of the ratio of n_ice/(n_ice + n_water)
        # input must be between zero and one
        def find_Gibbs(x):
            Optimizer.adjust_x(toy_system, x)
            return toy_system.calc_G()

        return find_Gibbs

    # optimizes Gibss of the given system
    def optimize(system):
        func = Optimizer.minimze_Gibbs_func(system)
        result = minimize_scalar(func, bounds=(0,1), method='bounded')
        optimal_x = result.x
        Optimizer.adjust_x(system, optimal_x)

    # adjust the ratio of the system to the desired value
    def adjust_x(system, x):
        n_total = system.subsystem.water.n + system.ice.n
        n_ice = system.ice.n
        x_current = n_ice/n_total
        dx = x_current - x
        dn_ice = dx*n_total
        system.move_ice(dn_ice)


