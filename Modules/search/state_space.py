import copy


class StateSpace:
    def __init__(self, state):
        self.state = state
        self.successors = self.generate_successors()

    def generate_successors(self):
        """
        Devuelve los sucesores del estado
        :return: sucesores
        """
        succesors = []

        # para cada movimiento se genera una accion segun la n del cubo
        for movement in ['B', 'b', 'D', 'd', 'L', 'l']:
            for i in range(self.state.cube.n):
                action = movement + str(i)
                succesors.append((action, self.__generate_state(action), 1))
        return succesors

    def __generate_state(self, action):
        """
        Se crea un nuevo estado a partir del estado actual.
        :param action: accion a aplicar sobre el estado
        :return: el nuevo estado generado al aplicar la accion
        """
        # copy.deepcopy(): copia el objeto completo de forma recursiva
        new_state = copy.deepcopy(self.state)
        new_state.apply_action(action)

        return new_state
