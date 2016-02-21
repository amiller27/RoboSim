import bge
from RoboSim.robot.proximitysensor import ProximitySensor

px1 = None
px2 = None
def setup():
    print('Algorithm setup')
    global px
    px1 = ProximitySensor(1)
    px2 = ProximitySensor(2)

def loop():
    print('Algorithm loop')
    #print(px.read())

