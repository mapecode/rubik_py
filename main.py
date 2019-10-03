from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube3x3.json")
    c = Cube(json_dict)
    print(c)
    c.move_down(0, True)
    c.move_down(0, True)
    c.move_down(0, True)
    c.move_down(0, True)

    c.move_down(0, False)
    c.move_down(0, False)
    c.move_down(0, False)
    c.move_down(0, False)


    print(c)




