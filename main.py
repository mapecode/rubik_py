from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube6x6.json")
    c = Cube(json_dict)
    print(c)
    c.move_down(0, True)
    c.move_left(0, True)
    c.move_back(0, True)
    c.move_down(1, True)
    c.move_left(1, True)
    c.move_left(2, True)
    c.move_back(3, True)


