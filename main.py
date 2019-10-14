from Modules.json import *
from Modules.cube import *
from time import *

if __name__ == '__main__':
    json_dict = read_json("Files/cube10x10.json")
    c = Cube(json_dict)
    print(c.key)
    print(c)
    sequence = "l3D1l1d0B0b5l2d1"
    c.apply_sequence(sequence)
    print(c.key)
    print(c)
    c.apply_sequence(invert_sequence(sequence))
    print(c.key)
    print(c)

