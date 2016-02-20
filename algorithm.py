import GameLogic
from RoboSim.robot.proximitysensor import ProximitySensor

def setup():
    print('Algorithm setup')
    px = ProximitySensor(1)

def loop():
    print('Algorithm loop')
    cont = GameLogic.getCurrentController()
    obj = cont.owner
    obj.applyTorque((0, 0, 10), False)
