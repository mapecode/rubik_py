import copy

class State:
    def __init__(self, cube):
        self.cube = cube

    # Sucesor (accion, estado, coste)
    def successor(self):
        """
        Devuelve los sucesores del estado
        :return: sucesores
        """
        succesors = []

        # para cada movimiento se genera una accion segun la n del cubo
        for movement in ['L', 'l', 'D', 'd', 'B', 'b']:
            for i in range(self.cube.n):
                action = movement + str(i)
                succesors.append((action, self.__generate_state(action), 1))
        return succesors

    def __generate_state(self, action):
        """
        Se crea un nuevo cubo a partir del principal para aplicar
        la posible accion
        :param action: accion a aplicar sobre la copia del cubo
        :return: el nuevo cubo generado a partir de la accion
        """
        # copy.deepcopy(): copia el objeto completo de forma recursiva
        new_cube = copy.deepcopy(self.cube)
        new_cube.apply_sequence(action)

        return new_cube
