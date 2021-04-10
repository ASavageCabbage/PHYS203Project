# Application entrypoint

import logging
import argparse

from testing.imports import list_all_modules
from testing.phase import *

from utils.system import System
from utils.optimize import optimize

def main():
    parser = argparse.ArgumentParser(description='Application entrypoint.')
    parser.add_argument(
        '--log', metavar='L', dest='log_level', type=str, nargs=1, help='Logging level (INFO, DEBUG, etc.)',
        default=[logging.INFO]
    )
    parser.add_argument(
        '--test', metavar='T', dest='test_tasks', type=str, nargs='+', help='Run tests (options: import, phase)',
        default=[]
    )
    parser.add_argument(
        '--init', metavar='I', dest='init_args', type=int, nargs=4,
        help='Initialize system to <temperature> <moles salt> <moles water> <moles ice>',
        default=[]
    )

    args = parser.parse_args()
    logging.basicConfig(format='%(levelname)s: %(message)s', level=args.log_level[0])
    logging.info("Started!")
    if 'import' in args.test_tasks:
        list_all_modules()
    if 'phase' in args.test_tasks:
        test_init_ice()
        test_init_water()
        test_init_salt()
        test_init_system()

    if args.init_args:
        temp, n_salt, n_water, n_ice = args.init_args
        logging.info(
            f"Initialized system at {temp} K with:\n"
          + f"{n_salt} mols of salt, {n_water} moles of liquid water, {n_ice} mols of ice"
        )
        system = System(n_salt, n_water, n_ice, temp)
        init_gibbs = system.calc_G()
        logging.info(f"Initial Gibbs Energy: {init_gibbs} J")
        optimize(system)
        final_gibbs = system.calc_G()
        delta_G = final_gibbs - init_gibbs
        heat = system.get_heat_flow()
        total_salt, dissolved_salt, total_water, total_ice = system.get_state()
        logging.info(
            f"At equilibrium, there are:\n"
          + f"{total_salt} mols of salt: {dissolved_salt} dissolved and {total_salt - dissolved_salt} precipitated\n"
          + f"{total_water} mols of liquid water\n"
          + f"{total_ice} mols of ice\n"
          + f"Delta G = {delta_G} J, Delta H = {heat} J"
        )

    logging.info("Finished!")

if __name__ == "__main__":
    main()
