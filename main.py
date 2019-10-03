from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube4x4.json")
    c = Cube(json_dict)
    print(c)
    c.move_back(0,True)
    print(c)






