from Modules.readjson import *
from Modules.cube import *
import Modules.constants as constants

if __name__ == '__main__':
    json_dict = read_json("Files/cube3x3.json")
    c = Cube(json_dict)
    print(c.key)
    sequence = "b2B1l0"
    c.apply_sequence(sequence)
    print(c.key)
    c.apply_sequence(invert_sequence(sequence))
    print(c.key)
