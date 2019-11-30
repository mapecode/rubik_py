from Modules.search.state import State
from Modules.search.state_space import StateSpace
import json


def read_json(path):
    """
    Funcion para la lectura del fichero json con la representacion del cubo
    :param path:
    :return:
    """
    with open(path, 'r') as file:
        return json.load(file)


class Problem:

    def __init__(self, path):
        self.initial_state = State(read_json(path))

    def is_goal(self, node, strategy):
        """
        Comprueba si el cubo es correcto
        :param state:
        :return: devuelve la comprobacion
        """
        if strategy is 'A' or strategy is 'Greedy':
            return node.state.is_correct(strategy, heuristic=node.heuristic)
        else:
            return node.state.is_correct(strategy)

    def generate_state_space(self, state):
        """
        Genera un nuevo espacio de estados a partir del estado
        :param state:
        :return: devuelve el espacio de estados
        """
        return StateSpace(state)
