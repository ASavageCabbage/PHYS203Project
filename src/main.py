# Application entrypoint

import logging
import sys

from testing.imports import list_all_modules

def tests():
    list_all_modules()

def main():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    logging.info("Started!")
    if sys.argv[1] == "test":
        tests()
    #
    # Rest of application functionality goes here
    #
    logging.info("Finished!")

if __name__ == "__main__":
    main()
