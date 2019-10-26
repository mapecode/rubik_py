import Modules.search.node

class Frontier:
    '''Frontera'''

    def __init__(self, node):
        self.frontier_list = []

    def insert(self, node):
        self.frontier_list.append(node)
        self.frontier_list.sort(key=lambda Node: Node.f)
        # self.frontier_list = sorted(key=lambda Node : Node.f) --> Segunda forma de ordenar lista original por key(f)

    def remove(self):
        self.frontier_list.remove()

    def is_empty(self):
        return len(self.frontier_list) == 0







