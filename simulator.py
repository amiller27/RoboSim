import bge
import algorithm
from RoboSim.robot.simbody import SimBody

setup_finished = False
def simulate():
    if setup_finished:
        algorithm.loop()
    else:
        body = SimBody()
        algorithm.setup()
        global setup_finished
        setup_finished = True
