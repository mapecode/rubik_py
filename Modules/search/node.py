class Tree_Node():
    '''Nodo Arbol'''

    # f: valor qe determinala posicion del nodo en su inserccion en la frontera, dado que es en orden asc suponemos BFS (f = depth)
    # action_cost: coste del camino desde el nodo inicial (raiz), hasta el nodo actual
    # action: accion llevada a cabo desde el padre al estado actual
    # parent: Tree_Node antecesor al nodo actual
    # state: correspondiente al id del cubo generado con md5 ¿?
    def __init__(self, state, f, action_cost=0, action=None, parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0;
        self.f = f
        self.path_cost = action_cost

        if parent is not None:
            self.depth = parent.depth + 1
            self.path_cost += parent.path_cost
