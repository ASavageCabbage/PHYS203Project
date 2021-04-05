# Takes copy of system objects and generates plot based on it
# updating a couple times a second

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import multiprocessing as mtp

class Graphics:

    ## CONSTANTS
    MAX_READING = 1# the minimum and maximum projected readings
    MIN_READING = 0
    MAX_SIZE = 1000 # maximum number of readings to display at once
    NUM_QUANTITIES = 2 # number of things being plotted
    LEGEND_LOCATION = 'upper right' # location of legend on graph
    COLOURS = ['blue', 'red'] # colour of lines
    LABELS = ["Water", "Salt Concentration"] # cell labels in legend
    RATE = 10 # refresh rate in milliseconds (every n ms)

    ## VARIABLES
    fig, ax = (None,None) # this is just initializing variables for the right scope
    yvalues = []
    lines = []
    pipe_opening = None
    animation_object = None

    ## METHODS

    # creates lines and plots that will be updated over time
    def initialize_plot():
        fig, ax = plt.subplots()
        ax.set_ylim((MIN_READING, MAX_READING))
        ax.set_xticks([])
        ax.set_title("")
        for i in range(0, NUMBER_CELLS):
            yvalues.append(np.zeros(MAX_SIZE))
            line, = ax.plot(yvalues[i], color=COLOURS[i])
            lines.append(line)
        ax.legend(LABELS[0:NUM_QUANTITIES], loc=LEGEND_LOCATION)

    # main process loop for graphics processes
    def main(terminal):
        pipe_opening = terminal
        initialize_plot()
        animation_object = FuncAnimation(fig, update, interval=RATE)
        plt.show()

    # checks terminal pipe for data, updates if there is any
    def update(_i):
        current_system = pipe_opening.recv()
        update_values(current_system)
        update_lines()

    # updates arrays of y-values, has to move them all left to do so
    def update_values(current_system):
        for j in range(0,2): # move all values forwards one
            to_change = yvalues[cell]
            for i in range(MAX_SIZE-1, 0, -1):
                to_change[i] = to_change[i-1]
        # put new values on the front
        yvalues[0][0] = current_system.liquid.n_water / (current_system.liquid.n_water + current_system.solid.n)
        yvalues[1][0] = current_system.liquid.n_salt / current_system.liquid.n_water

    # updates the data in the displayed lines
    def update_lines():
        for i in range(0, NUM_QUANTITIES):
            lines[i].set_ydata(yvalues[i])