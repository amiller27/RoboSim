import bge
from . import algorithm

setup_finished = False
def simulate():
    if setup_finished:
        algorithm.loop()
    else:
        algorithm.setup()
        global setup_finished
        setup_finished = True
