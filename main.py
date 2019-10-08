from Modules.readjson import *
from Modules.cube import *
from time import *

if __name__ == '__main__':
    json_dict = read_json("Files/cube6x6.json")
    c = Cube(json_dict)
    print(c.key)
    print(c)
    sequence = "b2l2l0L1D0B2d1D0L0L1b2b0b1l0l1L2D2D1d0B0B1b2B0"
    c.apply_sequence(sequence)
    print(c.key)
    print(c)
    c.apply_sequence(invert_sequence(sequence))
    print(c.key)
    print(c)
