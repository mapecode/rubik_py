#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: B1 - 11                      Curso: 2019 / 2020               ##
#############################################################################

from Modules.cube import *
from Modules.search.problem import Problem
from Modules.search.frontier import Frontier
from Modules.search.node import Node
from Modules.stack import Stack
import numpy
import time

id_node = 0


def limited_search(prob, strategy, max_depth):
    frontier = Frontier()
    cut_dic = {}

    def cut(n):
        if n.state.cube.hash in cut_dic:
            if n.function < cut_dic[n.state.cube.hash]:
                cut_dic[n.state.cube.hash] = n.function
                return n
        else:
            cut_dic[n.state.cube.hash] = n.function
            return n

        return None

    def create_node_list(successors_list, parent, max_depth, strategy):
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

        print(current_node)
        if prob.is_goal(current_node, strategy):
            return create_solution(current_node)
        else:
            successor_list = prob.generate_state_space(current_node.state).successors
            node_list = create_node_list(successor_list, current_node, max_depth, strategy)
            frontier.insert(node_list)

    return None


def search(prob, strategy, max_depth, depth_increment):
    current_depth = depth_increment

    n_sol = None
    global id_node
    while n_sol is None and current_depth <= max_depth:
        n_sol = limited_search(prob, strategy, current_depth)
        id_node = 0
        current_depth += depth_increment

    return n_sol


def write_solution(cube, strategy, solution):
    f = open("solution.txt", "w")
    f.write('Cube: '+cube+'\n')
    f.write('Strategy: '+strategy+'\n')
    f.write(solution)
    f.close()


def print_solution(solution):
    print('-----------------------------------------------------------------')
    print(solution)


def execution_time(initial_time):
    total_time = (time.time() - initial_time)
    if total_time < 60:
        print("\t* Tiempo de ejecucion:", round(total_time, 2), "segundos.")
    else:
        print("\t* Tiempo de ejecucion:", round(total_time / 60, 2), "minutos.")


if __name__ == '__main__':
    ti = time.time()
    cube = "Files/cube2x2.json"
    strategy = 'A'
    problem = Problem(cube)

    solution = search(problem, strategy, 6, 6)
    if solution is not None:
        print_solution(solution)
        write_solution(cube, strategy, solution)
    else:
        print("Sin solucion")
    print('----------------------------------------------------------------')
    execution_time(ti);
