# Application entrypoint

import logging
import argparse
import numpy as np
import matplotlib.pyplot as plt

from testing.imports import list_all_modules
from testing.phase import *

from utils.system import System
from utils.optimize import optimize, phase_diagram
from utils.phases import *

def optimize_once(temp, n_salt, n_water, n_ice):
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

TOTAL_SALT, DISSOLVED_SALT, TOTAL_WATER, TOTAL_ICE, HEAT_FLOW = range(5)
DIAGRAM_TYPES = {
    "ice": (
        lambda a: a[TOTAL_ICE],
        "Fraction of water frozen"
    ),
    "saturation": (
        lambda a: (a[DISSOLVED_SALT]/a[TOTAL_WATER]) / MAX_C,
        "Saltwater saturation (%)"
    ),
    "precipitate": (
        lambda a: a[TOTAL_SALT] - a[DISSOLVED_SALT],
        "Moles of salt precipitated per mole of water"
    ),
    "mixture": (
        lambda a: abs(a[TOTAL_WATER] - a[TOTAL_ICE]),
        "Highlights regions where water and ice coexist"
    ),
    "heat": (
        lambda a: a[HEAT_FLOW],
        "Heat flow into the system (J)"
    )
}

def generate_pd(t0, t1, s0, s1, n=100, dtype="ice", cmap="Greys"):
    logging.info(f"Generating <{dtype}> phase diagram for T = [{t0}, {t1}] K and moles of salt = [{s0}, {s1}]...")
    temps = np.linspace(t1, t0, n)
    salts = np.linspace(s0, s1, n)
    heatmap = np.array(phase_diagram(temps, salts))
    pick, label = DIAGRAM_TYPES[dtype]
    heatmap = [[pick(item) for item in row] for row in heatmap]

    fig, ax = plt.subplots()
    ax.set_xlabel("Salt Molarity (mols NaCl/mols H2O)")
    ax.set_ylabel("Temperature (C)")
    pos = ax.imshow(
        np.array(heatmap), cmap=cmap, interpolation="none",
        extent=[s0, s1, t0-273.15, t1-273.15], aspect=(s1-s0)/(t1-t0)
    )
    cbar = fig.colorbar(pos, ax=ax)
    cbar.set_label(label)
    plt.show()

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
        '--init', metavar='I', dest='init_args', type=float, nargs=4,
        help='Initialize system to <temperature> <moles salt> <moles water> <moles ice>',
        default=None
    )
    parser.add_argument(
        '--phase_diagram', metavar='PD', dest='pd_args', type=float, nargs=4,
        help='Generate a phase diagram of the salt-water system in <min temp> <max temp> <min salt> <max salt>',
        default=None
    )
    parser.add_argument(
        '--diagram_style', metavar='DS', dest='pd_options', type=str, nargs='+',
        help='(Optional) specify type of phase diagram and colour scheme: <ice, saturation, precipitate, mixture> <cmap>',
        default=None
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
        optimize_once(*args.init_args)
    
    if args.pd_args:
        dtype = None
        cmap = None
        if args.pd_options:
            dtype = args.pd_options[0]
            if len(args.pd_options) > 1:
                cmap = args.pd_options[1]
        generate_pd(
            *args.pd_args,
            dtype=dtype if dtype else "ice",
            cmap=cmap if cmap else "Greys"
        )

    logging.info("Finished!")

if __name__ == "__main__":
    main()
