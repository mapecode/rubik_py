import Modules.state as state


class Tree_Node():
    '''Nodo Arbol'''

    # f: valor qe determinala posicion del nodo en su inserccion en la frontera, dado que es en orden asc suponemos BFS (f = depth)
    # road_cost: coste del camino desde el nodo inicial (raiz), hasta el nodo actual
    # action: accion llevada a cabo desde el padre al estado actual
    # parent: Tree_Node antecesor al nodo actual
    # state: correspondiente al id del cubo generado con md5 ¿?
    def __init__(self, state, action_cost, action=None, parent=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = self.f = 0  # Tener en cuenta
        self.cost = action_cost

        if parent is not None:
            self.depth = self.f = parent.depth + 1
            self.cost += parent.cost
