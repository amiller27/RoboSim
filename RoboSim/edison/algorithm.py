import GameLogic
from .robot import *

def setup():
    print('Algorithm setup')

def loop():
    print('Algorithm loop')
    cont = GameLogic.getCurrentController()
    obj = cont.owner
    obj.applyTorque((0, 0, 0.5), False)
