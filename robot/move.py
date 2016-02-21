import bge
import bpy.path
import json

class Move:
    instances = []

    def __init__(self):
        abs_path = bpy.path.abspath("//")
        with open(abs_path + 'description.json') as desc_file:
            desc = json.loads(desc_file.read())
        scene = bge.logic.getCurrentScene()
        simbody_name = desc['simbody']['top_level_model']
        self.simbody = scene.objects[simbody_name]

        self.simbody.setDamping(0.6, 0.6)

        Move.instances.append(self)

    def forward(self):
        self.simbody.setLinearVelocity([0, 0.4, 0], True)

    def backward(self):
        self.simbody.setLinearVelocity([0, -0.4, 0], True)

    def left(self):
        self.simbody.setAngularVelocity([0, 0, 2], True)

    def right(self):
        self.simbody.setAngularVelocity([0, 0, -2], True)
