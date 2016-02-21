from RoboSim.robot.proximitysensor import ProximitySensor
from RoboSim.robot.steppermove import StepperMove

px_right = None
px_left = None
move = None

def setup():
    print('Algorithm setup')
    global px_right, px_left, move
    px_right = ProximitySensor(6)
    px_left = ProximitySensor(13)
    move = StepperMove()

i = 0
queue = []
def loop():
    global i
    if queue:
        (queue.pop(0))()
        return
    #print('Algorithm loop')
    #print(px_right.read(), px_left.read())
    if px_right.read():
        queue.extend(lambda : move.backward() for i in range(10))
        queue.extend(lambda : move.left() for i in range(10))
        #else:
            #print("moving left")
            #move.right()
    elif px_left.read():
        print("moving right")
        queue.extend(lambda : move.backward() for i in range(10))
        queue.extend(lambda : move.right() for i in range(10))
        #move.left()
    else:
        print("moving forward")
        move.forward()
