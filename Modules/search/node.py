class Node:

    def __init__(self, id_node, parent, state, action_cost, strategy, action):
        self.id_node = id_node
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = action_cost

        if parent is not None:
            self.cost = parent.cost + action_cost
            self.depth = parent.depth + 1
        else:
            self.depth = 0
            self.cost = action_cost

        self.function = round(self.define_f(strategy), 2)

    def define_f(self, strategy):
        if strategy is 'Breadth':
            return self.depth
        elif strategy is 'Uniform':
            return self.cost
        elif strategy is 'Depth':
            return 1 / (self.depth + 1)

    def __str__(self):
        return '[' + str(self.id_node) + ']([' + str(self.action) + ']' + self.state.cube.hash + ',c=' + str(
            self.cost) + ',p=' + str(
            self.depth) + ',f=' + str(
            self.function) + ')'

    def __gt__(self, other):
        """
        Utilizado en la cola de prioridad para comprarar dos nodos
        """
        return self.function > other.function
