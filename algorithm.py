import bge
from RoboSim.robot.proximitysensor import ProximitySensor
from RoboSim.robot.steppermove import StepperMove

px_right = None
px_left = None
move = None

def setup():
    print('Algorithm setup')
    global px_right, px_left, move
    px_right = ProximitySensor(1)
    px_left = ProximitySensor(2)
    move = StepperMove()

i = 0
queue = []
def loop():
    global i
    if queue:
        (queue.pop())()
        return
    #print('Algorithm loop')
    #print(px_right.read(), px_left.read())
    if px_right.read():
        if px_left.read():
            queue.extend(lambda : move.backward() for i in range(10))
            queue.extend(lambda : move.right() for i in range(10))
        else:
            move.left()
    elif px_left.read():
        move.right()
    else:
        move.forward()
