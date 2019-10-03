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
    # Ir hacia atras
    c.move_back(3, False)
    c.move_left(2, False)
    c.move_left(1, False)
    c.move_down(1, False)
    c.move_back(0, False)
    c.move_left(0, False)
    c.move_down(0, False)
    print(c)

