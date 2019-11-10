class Node:
    '''Nodo del Árbol'''

    # f: valor que determina la posicion del nodo en su inserccion en la frontera, depende de la estrategia elegida.
    # action_cost: coste del camino desde el nodo actual hasta su nodo sucesor.
    # action: accion llevada a cabo desde el nodo actual al nodo sucesor.
    # parent: Node antecesor al nodo actual.

    def __init__(self, parent, state, action_cost, strategy, action):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = action_cost

        if parent is None:
            self.path_cost = 0
            self.depth = 0
        else:
            self.depth = parent.depth + 1
            self.path_cost += parent.path_cost

        self.function = self.define_f(strategy)

    def define_f(self, strategy):
        if strategy is 'anchura':
            return self.depth
        elif strategy is 'costo':
            return self.path_cost
