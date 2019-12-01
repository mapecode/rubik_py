#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: B1 - 11                      Curso: 2019 / 2020               ##
#############################################################################

from Modules.search.problem import Problem
from Modules.search.frontier import Frontier
from Modules.search.node import Node
from Modules.stack import Stack
from Modules.color import Color
import time
import sys

id_node = 0


def limited_search(prob, strategy, max_depth):
    """
    Funcion para aplicar la busqueda acotada
    :param prob: representa el problema del que se parte
    :param strategy: estrategia a aplicar
    :param max_depth: maxima profundidad a la se debe llegar
    :return: solucion si se encuentra, None si no se encuentra
    """
    frontier = Frontier()
    cut_dic = {}

    def cut(n):
        """
        Funcion de poda de un nodo que, si ya ha sido añadido a la frontera se comprueba si tiene mejor f.
        En caso afirmativo se introducira, y en caso contrario no.
        :param n: nodo candidato a podar
        :return:
        """
        if n.state.cube.hash in cut_dic:
            if n.function < cut_dic[n.state.cube.hash]:
                cut_dic[n.state.cube.hash] = n.function
                return n
        else:
            cut_dic[n.state.cube.hash] = n.function
            return n

        return None

    def create_node_list(successors_list, parent, max_depth, strategy):
        """
        Funcion que crea los nodos hijos de un nodo. Para cada posible nodo que se crea se llama a la funcion de poda
        para decidir si se va a introducir a la frontera
        :param successors_list: lista de sucesores de un nodo
        :param parent: padre del nodo
        :param max_depth: profundidad maxima
        :param strategy: estrategia aplicada
        :return: la lista de nodos generada
        """
        node_list = []
        global id_node

        if parent.depth < int(max_depth):
            for successor in successors_list:
                action, state, cost = successor
                n = cut(Node(id_node, parent, state, cost, strategy, action))

                if n is not None:
                    node_list.append(n)

                id_node += 1

        return node_list

    def create_solution(node):
        """
        Funcion para crear la solucion al encontrar el estado objetivo, recorriendo el camino seguido gracias al
        predecesor o padre de cada nodo. Este camino se invertira para tener la secuencia de acciones aplicadas desde
        el cubo inicial
        :param node: nodo con el estado objetivo
        :return: string con la secuencia de acciones para resolver el cubo inicial, una por linea
        """
        stack = Stack()
        node_aux = node
        solution = []

        while node_aux.parent is not None:
            stack.push(node_aux)
            node_aux = node_aux.parent

        stack.push(node_aux)

        while not stack.is_empty():
            solution.append(str(stack.pop()))

        return '\n'.join(solution)

    global id_node
    frontier.insert([Node(id_node, None, prob.initial_state, 0, strategy, None)])
    id_node += 1

    while not frontier.is_empty():
        current_node = frontier.remove()
        if prob.is_goal(current_node, strategy):
            return create_solution(current_node)
        else:
            successor_list = prob.generate_state_space(current_node.state).successors
            node_list = create_node_list(successor_list, current_node, max_depth, strategy)
            frontier.insert(node_list)

    return None


def search(prob, strategy, max_depth, depth_increment):
    """
    Funcion que aplica la busqueda. Llamara a la funcion de busqueda acotada segun la profundidad maxima e incremento
    de esta elegidos
    :param prob: representa el problema del que partimso
    :param strategy: estrategia a aplicar
    :param max_depth: maxima profundidad a la que se llegara
    :param depth_increment: incremento de la profundidad
    :return: la solucion si se encuentra
    """
    current_depth = depth_increment

    sol = None
    global id_node

    print("\nBuscando solucion ...")

    while sol is None and current_depth <= max_depth:
        sol = limited_search(prob, strategy, current_depth)
        id_node = 0
        current_depth += depth_increment

    return sol


def write_solution(cube, strategy, solution):
    """
    Escribe la solucion en el fichero 'solution.txt'
    :param cube: fichero del cubo inicial
    :param strategy: estrategia seguida
    :param solution: secuencia de pasos hasta el estado objetivo
    :return:
    """
    f = open("solution.txt", "w")
    f.write('* Cube: ' + cube + '\n' + '* Strategy: ' + strategy.upper() + '\n\n* Solution: \n')
    f.write(solution)
    f.close()


def execution_time(initial_time):
    """
    Calcula el tiempo de ejecucion dado un tiempo inicial
    :param initial_time: tiempo inicial
    :return:
    """
    total_time = (time.time() - initial_time)
    if total_time < 60:
        print(Color.BOLD + "\t* Tiempo de ejecucion:", round(total_time, 2), "segundos.\n" + Color.END)
    else:
        print(Color.BOLD + "\t* Tiempo de ejecucion:", round(total_time / 60, 2), "minutos.\n" + Color.END)


def check_argv():
    """
    Comprueba los argumentos y obtiene los datos necesarios para iniciar la busqueda
    :return: la profundidad maxima, el incremento de la profundidad, la estrategia, el problema del que se parte
    """
    global depth_increment, max_depth, strategy, problem
    strategies = ['breadth', 'limited_depth', 'iterative_depth', 'simple_depth', 'cost', 'a*', 'greedy']

    if len(sys.argv) is not 5:
        print(Color.BOLD + Color.RED + 'Error en los argumentos \n'
                                       'Uso correcto: python3 rubik.py <max_depth> <depth_increment> '
                                       '<strategy> <cube.json>' + Color.END)
        exit()
    else:
        try:
            max_depth = int(sys.argv[1])
            depth_increment = int(sys.argv[2])
        except Exception as e:
            print(Color.BOLD + Color.RED + 'Error en los argumentos: ' + str(e) + Color.END)
            exit()

        strategy = sys.argv[3].lower()
        if strategy not in strategies:
            print(Color.BOLD + Color.RED + "Estrategia '" + strategy + "' incorrecta" + Color.END)
            print('Estrategias validas:', ', '.join(strategies))
            exit()
        problem = Problem(sys.argv[4])

    return max_depth, depth_increment, strategy, problem


if __name__ == '__main__':

    max_depth, depth_increment, strategy, problem = check_argv()

    ti = time.time()

    solution = search(problem, strategy, depth_increment, max_depth)
    if solution is not None:
        print('--------------------------------------------------------------------------')
        print("* Cube: " + problem.path + "\n* Strategy: " + strategy.upper() + "\n\n* Solution: ")
        print(Color.BOLD + solution + Color.END)
        write_solution(problem.path, strategy, solution)
    else:
        print("Sin solucion")
    print('--------------------------------------------------------------------------')
    execution_time(ti)
