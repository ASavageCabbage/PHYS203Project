# parent (abstract) class for a phase
#
# this still needs to be finished, I just wanted to move
# on to making an implementation to get a better idea of
# what's going on here
# THIS IS ONLY INTENDED TO SPECIFY WHAT SYSTEM ACCESS FUNCTIONS
# ARE NEEDED, NOTHING ELSE

class Phase:

    ## System access functions

    # adds n moles of phase to the phase object, this should handle updating
    # gibbs energy and internal energy itself
    def add_moles(self, n):
        pass

    # adds/removes an amount of energy e from the system as heat, and updates
    # temperature accordingly
    def add_heat(self, e):
        pass
