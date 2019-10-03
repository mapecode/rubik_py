from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube3x3.json")
    c = Cube(json_dict)
    print(c)
<<<<<<< HEAD
    c.move_left(0, True)
    print(c)
=======
    c.move_down(0, True)
    c.move_down(0, True)
    c.move_down(0, True)
    c.move_down(0, True)

    c.move_down(0, False)
    c.move_down(0, False)
    c.move_down(0, False)
    c.move_down(0, False)


    print(c)



>>>>>>> 1c392eb4cc21dce567a15adfbfecfe9de55680e4

