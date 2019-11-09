from Modules.cube import Cube
from Modules.json import *
from Modules.search.state import *

class problem:

    def __init__(self, path):
        self.state = State()
        json_dict = read_json(path)
        self.initial = Cube(json_dict)

    def is_objective(self, state):
        pass
