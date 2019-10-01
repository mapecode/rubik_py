from Modules.readjson import *
from Modules.cube import *

if __name__ == '__main__':
<<<<<<< HEAD
    json_dict = read("Files/cube10x10.json")
=======
    json_dict = read("Files/cube4x4.json")
>>>>>>> 6ff237566427cba2043e496b3b47d14d8561621f
    id_string, n = to_str(json_dict)
    c = Cube(id_string, n)
    print(c)
    c.move_left(0, True)
    print(c)
