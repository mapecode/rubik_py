from Modules.readjson import *
from Modules.cube import *

if __name__ == '__main__':
    json_dict = read("Files/cube10x10.json")
    id_string, n = to_str(json_dict)
    c = Cube(id_string, n)
    print(c)
    c.move_left(0, True)
    print(c)
