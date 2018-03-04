import bge
import bpy
import bpy.path
import json
import mathutils
import os.path

class ProximitySensor:
    instances = []

    def __init__(self, pin):

        abs_path = bpy.path.abspath("//")

        self.pin = pin

        with open(abs_path + 'description.json') as desc_file:
            desc = json.loads(desc_file.read())
        sensors_for_pin = list(filter(
            lambda sens: sens['type'] == 'ProximitySensor' and sens['pin'] == self.pin,
            desc['sensors']))
        if len(sensors_for_pin) != 1:
            raise ValueError('Unable to find unique sensor for pin ' + str(self.pin))
        self.desc = sensors_for_pin[0]

        self.activated = False

        scene = bge.logic.getCurrentScene()

        simbody_name = desc['simbody']['top_level_model']
        simbody = scene.objects[simbody_name]

        blend_path = os.path.dirname(os.path.realpath(__file__)) + '/models/proximitysensor.blend'
        if blend_path not in bge.logic.LibList():
            bge.logic.LibLoad(blend_path, 'Scene', async = False)

        new_sensor = scene.addObject('ProximitySensor', simbody, 0)
        new_sensor.setParent(simbody)
        new_sensor.localPosition = self.desc['location']
        new_sensor.localOrientation = mathutils.Euler(self.desc['rotation'], 'XYZ')

        new_sensor['robosim_sensor'] = self
        self.sensor = new_sensor

        ProximitySensor.instances.append(self)

    def _set_activated(self, activated):
        self.activated = activated

    def read(self):
        return self.activated

def activate():
    print('activate called')
    blender_sensor = bge.logic.getCurrentController()
    blender_sensor.owner['robosim_sensor']._set_activated(blender_sensor.sensors['Radar'].positive)
