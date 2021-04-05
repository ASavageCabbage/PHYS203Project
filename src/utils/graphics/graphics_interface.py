# methods to send graphics data to process

import multiprocessing as mtp
from utils.graphics import Graphics

class Graphics_Interface:

    ## VARIABLES
    recieve, pipe, graph_process = None, None, None

    ## METHODS

    # starts graphics process    
    def initize_graphics():
        try:
            recieve, pipe = mtp.Pipe(False)
            graph_process = mtp.Process(target=rtp.main, args=(recieve,))
            graph_process.daemon = True
            graph_process.start()
        except mtp.ProcessError as err:
            raise # propogate exception

    # mass current instance of system to graphics process
    def pass_system(current_system):
        pipe.send(current_system.deep_copy()) # this needs to be a deep copy
        # otherwise there will be race conditions
