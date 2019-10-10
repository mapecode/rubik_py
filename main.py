from Modules.json import *
from Modules.cube import *
from time import *

if __name__ == '__main__':
    json_dict = read_json("Files/cube10x10.json")
    c = Cube(json_dict)
    print(c.key)
    sequence = "l3"
    c.apply_sequence(sequence)
    print(c.key)
