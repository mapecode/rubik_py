import Modules.cube

class state():
    def __init__(self, cube):
        self.cube = cube

    # Sucesor (accion, estado, coste)
    def successor(self):
        successors = []

