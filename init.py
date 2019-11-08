#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: B1 - 11                      Curso: 2019 / 2020               ##
#############################################################################

from Modules.json import *
from Modules.cube import *
from Modules.search.state import *

if __name__ == '__main__':
    json_dict = read_json("Files/cube3x3.json")
    c = Cube(json_dict)

    s = State(c)
    sucs = s.successor()

    for suc in sucs:
        print(suc[1])
