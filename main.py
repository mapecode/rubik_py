from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read("Files/cube3x3.json")
    id_string, n = to_str(json_dict)
    c = Cube(id_string, n)
    #c.move_back(1, True)
    print(c)





