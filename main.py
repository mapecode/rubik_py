from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube3x3.json")
    c = Cube(json_dict)
    print(c)
    sequence = "b2"
    c.apply_sequence(sequence)
    print(c)
    c.apply_sequence(invert_sequence(sequence))
    print(c)
