from Modules.search.state import State
from Modules.search.state_space import StateSpace
from Modules.color import Color
import json


def read_json(path):
    """
    Funcion para la lectura del fichero json con la representacion del cubo
    :param path: ruta del fichero json
    :return:
    """
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(Color.BOLD + Color.RED + 'Error en ' + path + ': ' + str(e) + Color.END)
        exit()


class Problem:

    def __init__(self, path):
        """
        Constructor de la clase problema
        :param path: ruta del fichero json
        """
        self.path = path
        self.initial_state = State(read_json(self.path))

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
