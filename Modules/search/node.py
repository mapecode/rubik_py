class Node():
    '''Nodo del Árbol'''
    # f: valor que determina la posicion del nodo en su inserccion en la frontera, depende de la estrategia elegida.
    # action_cost: coste del camino desde el nodo actual hasta su nodo sucesor.
    # action: accion llevada a cabo desde el nodo actual al nodo sucesor.
    # parent: Node antecesor al nodo actual.

    def __init__(self, state, f, action, action_cost, parent):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0;
        self.f = f
        self.path_cost = action_cost

        if parent is not None:
            self.depth = parent.depth + 1
            self.path_cost += parent.path_cost
