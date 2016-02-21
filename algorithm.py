import bge
import GameLogic
from RoboSim.robot.proximitysensor import ProximitySensor

px = None
def setup():
    print('Algorithm setup')
    global px
    px = ProximitySensor(1)

def loop():
    print('Algorithm loop')
    cont = GameLogic.getCurrentController()
    obj = cont.owner
    #obj.applyTorque((0, 0, 0.5), False)
    #print(px.read())

    bge.logic.getCurrentScene().objects['simbody'].applyForce((0, 10, 0))
