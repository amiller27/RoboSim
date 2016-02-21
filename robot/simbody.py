import bge
from bge import logic
import bpy
import json
import mathutils
import os.path

status = None

class SimBody:

    def __init__(self):
        print("Simbody Initalizing")
        abs_path = bpy.path.abspath("//")
        module_path = os.path.dirname(os.path.abspath(__file__))

        with open(abs_path + 'description.json') as desc_file:
            desc = json.loads(desc_file.read())

        try:
            model_name = desc['simbody']['model']
            top_level_name = desc['simbody']['top_level_model']
        except KeyError as e:
            print(e)

        global status
        status = logic.LibLoad(module_path + '/models/' + model_name, "Scene")

        scene = logic.getCurrentScene()
        self.model = scene.addObject(top_level_name, 'Empty')

        camera = scene.objects['Camera']
        camera.setParent(self.model)
        camera.localPosition = [0, -2, 1]
        camera.localOrientation = mathutils.Euler([1.2, 0, 0], 'XYZ')
        camera.near = 1
