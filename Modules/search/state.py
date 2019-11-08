import copy

class state():
    def __init__(self, cube):
        self.cube = cube

    # Sucesor (accion, estado, coste)
    def successor(self):
        sucs = []

        for i in range(3):
            cube = copy.copy(self.cube)

            if i == 0:
                for j in range(cube.n):
                    
            elif i == 1:

            elif i == 2:

