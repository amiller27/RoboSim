import bge
from bge import logic
import bpy
import json

status = None

class SimBody:
    def __init__(self):
        abs_path = bpy.path.abspath("//")

        with open(abs_path + 'description.json') as desc_file:
            desc = json.loads(desc_file.read())
        # model_name = list(filter(
        #    lambda sens: sens['type'] == 'SimBody',
        #    desc['sensors']))
        try:
            model_name = desc['simbody']['model']
        except KeyError as e:
            print(e)

        print("Simbody Initalizing")
        if len(logic.LibList()) < 1:
            #print(logic.LibList())
            global status
            print("\n\nStarting Loading")
            status = logic.LibLoad(abs_path + model_name, "Scene", verbose = True,  async=False)
            print("Done Loading\n\n")
        else:
            return
        print("Libloaded: " + status.libraryName)


        

        scene = logic.getCurrentScene()
        Cone = scene.addObject("ConeMan", "Plane")

    def read(self):
        pass
