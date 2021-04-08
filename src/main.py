# Application entrypoint

import logging
import argparse

from testing.imports import list_all_modules
from testing.phase import *

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
    args = parser.parse_args()
    logging.basicConfig(format='%(levelname)s: %(message)s', level=args.log_level[0])
    logging.info("Started!")
    if 'import' in args.test_tasks:
        list_all_modules()
    if 'phase' in args.test_tasks:
        test_init_ice()
        test_init_water()
        test_init_salt()
    #
    # Rest of application functionality goes here
    #
    logging.info("Finished!")

if __name__ == "__main__":
    main()
