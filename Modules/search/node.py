class Node():
    '''Nodo del Árbol'''
    # f: valor qe determinala posicion del nodo en su inserccion en la frontera, dado que es en orden asc suponemos BFS (f = depth)
    # action_cost: coste del camino desde el nodo inicial (raiz), hasta el nodo actual
    # action: accion llevada a cabo desde el padre al estado actual
    # parent: Tree_Node antecesor al nodo actual

    def __init__(self, state, f, action, action_cost, parent):
        # crear self.id como variable estatica, pasra asi en cada creación de u nodo se incremente este valor en 1.
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0;
        self.f = f
        self.path_cost = action_cost

        if parent is not None:
            self.depth = parent.depth + 1
            self.path_cost += parent.path_cost
