from Modules.search.state import State
from Modules.search.state_space import StateSpace


class Problem:

    def __init__(self, path):
        self.initial_state = State(path)

    def is_goal(self, state):
        """
        Comprueba si el cubo es correcto
        :param state:
        :return: devuelve la comprobacion
        """
        return state.is_correct()

    def generate_state_space(self, state):
        """
        Genera un nuevo espacio de estados a partir del estado
        :param state:
        :return: devuelve el espacio de estados
        """
        return StateSpace(state)
