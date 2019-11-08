from queue import PriorityQueue

class Frontier:
    '''Frontera'''

    def __init__(self, node):
        self.frontier_list = []
        self.queue = PriorityQueue()

    def insert(self, node):
        self.queue.put((node.f, node))

    def remove(self):
        self.frontier_list.remove()

    def is_empty(self):
        return len(self.frontier_list) == 0
