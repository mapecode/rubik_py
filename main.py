#############################################################################
##                       Sistemas Inteligentes                             ##
##    Grupo: B1 - 11                      Curso: 2019 / 2020               ##
#############################################################################

from Modules.json import *
from Modules.cube import *
from Modules.search.problem import Problem
from Modules.search.frontier import Frontier
from Modules.search.node import Node


def create_node_list(successors_list, parent, max_depth, strategy):
    node_list = []

    if parent.depth < int(max_depth):
        for successor in successors_list:
            action, state, cost = successor
            node_list.append(Node(parent, state, cost, strategy, action))

    return node_list


def limited_search(prob, strategy, max_depth):
    def create_solution(node):
        return node.state.cube

    frontier = Frontier()
    frontier.insert([Node(None, prob.initial_state, 0, strategy, None)])
    solution = False
    current_node = None

    while not solution and not frontier.is_empty():
        current_node = frontier.remove()
        current_state = current_node.state

        if prob.is_goal(current_state):
            solution = True
        else:
            successor_list = prob.generate_state_space(current_state).successors
            node_list = create_node_list(successor_list, current_node, max_depth, strategy)
            frontier.insert(node_list)
    if solution:
        return create_solution(current_node)
    else:
        return None


def search(prob, strategy, max_depth, depth_increment):
    current_depth = depth_increment

    n_sol = None

    while n_sol is None and current_depth <= max_depth:
        n_sol = limited_search(prob, strategy, max_depth)
        current_depth += depth_increment

    return n_sol


if __name__ == '__main__':
    problem = Problem("Files/cube2x2.json")

    solution = search(problem, "anchura", 6, 1)

    print(solution)

"""
    # primera impresion del original antes de aplicar la creacion de sucesores
    print(c)

    s = State(c)
    sucs = s.successor()

    for suc in sucs:
        print(suc[1])

    # comprobacion original
    print(c)
    
    
"""
