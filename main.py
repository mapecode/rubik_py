from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read("Files/cube3x3.json")
    #id_string = to_str(json_dict)
    c = Cube(json_dict)
    print(c)
    c.move_back(0,True)
    print(c)






