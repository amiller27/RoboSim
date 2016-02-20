import bge
from bge import logic
import bpy
import json

status = None

class SimBody:

    model = None

    def __init__(self):
        abs_path = bpy.path.abspath("//")

        with open(abs_path + 'description.json') as desc_file:
            desc = json.loads(desc_file.read())

        try:
            model_name = desc['simbody']['model']
        except KeyError as e:
            print(e)

        print("Simbody Initalizing")
        if len(logic.LibList()) < 1:
            global status
            status = logic.LibLoad(abs_path + model_name, "Scene", verbose = True,  async=False)
        else:
            return
        print("Libloaded: " + status.libraryName)

        scene = logic.getCurrentScene()
        model = scene.addObject(model_name[:-6], "Plane")

    def read(self):
        pass
