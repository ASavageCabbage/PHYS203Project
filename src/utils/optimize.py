# methods used to optimize (minimze) the Gibbs energy of the system
# TODO: Do this legit. Right now I'm just trying something

import logging
import numpy as np
from scipy.optimize import minimize_scalar
from copy import deepcopy

from utils.system import System

class Optimizer:

    # constructs and returns minimizng function for particular system
    def minimze_Gibbs_func(system):
        
        # function that returns the Gibbs energy for a particular system,
        # as a function of the ratio of n_ice/(n_ice + n_water)
        # input must be between zero and one
        def find_Gibbs(x):
            toy_system = deepcopy(system)
            Optimizer.adjust_x(toy_system, x)
            return toy_system.calc_G()

        print(find_Gibbs(0),find_Gibbs(1))
        return find_Gibbs

    # optimizes Gibss of the given system
    def optimize(system):
        func = Optimizer.minimze_Gibbs_func(system)
        result = minimize_scalar(func)
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


