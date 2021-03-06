# Testing imports

import logging

import utils.phases, utils.absolute, utils.differential, utils.system, utils.optimize

PACKAGES = [utils.phases, utils.absolute, utils.differential, utils.system, utils.optimize]

def list_all_modules():
    for pkg in PACKAGES:
        all_names = dir(pkg)
        public = [n for n in all_names if not n.startswith('_')]
        private = [n for n in all_names if n.startswith('_')]
        logging.debug(f"Imported package {getattr(pkg, '__name__')}\n"
                    + f"Public attributes: {public}\nPrivate attributes: {private}")
