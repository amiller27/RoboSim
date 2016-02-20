import bge
import bpy
import json

class ProximitySensor:
    def __init__(self, pin):
        self.pin = pin
        with open('description.json') as desc_file:
            desc = json.loads(desc_file.read())
        sensors_for_pin = list(filter(
            lambda sens: sens['type'] == 'ProximitySensor' and sens['pin'] == self.pin,
            desc['sensors']))
        if len(sensors_for_pin) != 1:
            raise ValueError('Unable to find unique sensor for pin ' + str(self.pin))
        self.desc = sensors_for_pin[0]

        bpy.ops.mesh.primitive_ico_sphere_add()

    def read(self):
        pass

