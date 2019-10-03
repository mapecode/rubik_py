from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube6x6.json")
    c = Cube(json_dict)

    c.move_back(0, False)
    c.move_back(0, False)
    c.move_back(1, False)
    c.move_back(3, True)
    print(c)
    c.move_back(0, True)
    c.move_back(0, True)
    c.move_back(1, True)
    c.move_back(3, False)
    print(c)

