#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: B1 - 11                      Curso: 2019 / 2020               ##
#############################################################################

from Modules.json import *
from Modules.cube import *
from time import *

if __name__ == '__main__':
    json_dict = read_json("Files/cube10x10.json")
    c = Cube(json_dict)
    print(c)
    print(c.is_correct())
    c.apply_sequence("l0")
    print(c.is_correct())
