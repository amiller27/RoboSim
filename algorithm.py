import bge
from RoboSim.robot.proximitysensor import ProximitySensor

px = None
def setup():
    print('Algorithm setup')
    global px
    px = ProximitySensor(1)

def loop():
    print('Algorithm loop')
    #print(px.read())

