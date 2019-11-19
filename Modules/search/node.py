class Node:

    def __init__(self, id_node, parent, state, action_cost, strategy, action):
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
        if self.strategy is 'Breadth':
            return self.depth
        elif self.strategy is 'Uniform':
            return self.cost
        elif self.strategy is 'Depth':
            return 1 / (self.depth + 1)
        elif self.strategy is 'A*':
            self.heuristic = self.state.calculate_heuristic()
            return self.heuristic + self.cost
        elif self.strategy is 'Greedy':
            self.heuristic = self.state.calculate_heuristic()
            return self.heuristic

    def __str__(self):
        if self.strategy is 'A*' or self.strategy is 'Greedy':
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
        Utilizado en la cola de prioridad para comprarar dos nodos
        """
        if self.function == other.function:
            return self.id_node > other.id_node
        else:
            return self.function > other.function
