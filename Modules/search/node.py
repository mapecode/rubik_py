class Node:

    def __init__(self, id_node, parent, state, action_cost, strategy, action):
        """
        Constructor de la clase nodo
        :param id_node: identificador del nodo
        :param parent: nodo padre
        :param state: estado del nodo
        :param action_cost: coste de llegar al nodo
        :param strategy: estrategia utilizada
        :param action: accion aplicada
        """
        self.id_node = id_node
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = action_cost
        self.strategy = strategy
        self.heuristic = None

        if parent is not None:
            self.cost = parent.cost + action_cost
            self.depth = parent.depth + 1
        else:
            self.depth = 0
            self.cost = action_cost

        self.function = round(self.define_f(), 2)

    def define_f(self):
        """
        Define la funcion segun la estrategia aplicada en la ejecucion
        :return: calculo de f
        """
        if self.strategy.lower() == 'breadth':
            return self.depth
        elif self.strategy.lower() == 'cost':
            return self.cost
        elif self.strategy.lower() == 'a':
            self.heuristic = self.state.calculate_heuristic()
            return self.heuristic + self.cost
        elif self.strategy.lower() == 'greedy':
            self.heuristic = self.state.calculate_heuristic()
            return self.heuristic
        else:
            return 1 / (self.depth + 1)

    def __str__(self):
        """
        Metodo redefinido para la impresion de un objeto de tipo nodo
        :return: string que representa el objeto
        """
        if self.strategy.lower() == 'a' or self.strategy.lower() == 'greedy':
            return '[' + str(self.id_node) + ']([' + str(self.action) + ']' + self.state.cube.hash + ',c=' + str(
                self.cost) + ',p=' + str(
                self.depth) + ',h=' + str(self.heuristic) + ',f=' + str(
                self.function) + ')'
        else:
            return '[' + str(self.id_node) + ']([' + str(self.action) + ']' + self.state.cube.hash + ',c=' + str(
                self.cost) + ',p=' + str(
                self.depth) + ',f=' + str(
                self.function) + ')'

    def __gt__(self, other):
        """
        Metodo de la operacion '>' redefinido, utilizado en la cola de prioridad para comprarar nodos al insertar
        """
        if self.function == other.function:
            return self.id_node > other.id_node
        else:
            return self.function > other.function
