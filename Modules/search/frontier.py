import heapq


class Frontier:
    def __init__(self):
        self.__queue = []

    def insert(self, nodes):
        for node in nodes:
            heapq.heappush(self.__queue, node)

    def remove(self):
        return heapq.heappop(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0


"""class Frontier:
    def __init__(self):
        self.__queue = PriorityQueue()

    def insert(self, nodes):
        for node in nodes:
            self.__queue.put_nowait(node)

    def remove(self):
        return self.__queue.get_nowait()

    def is_empty(self):
        return self.__queue.empty()"""

"""
class Frontier:
    def __init__(self):
        self.frontier_list = []

    def insert(self, nodes):
        for node in nodes:
            self.frontier_list.append(node)

        self.frontier_list = sorted(self.frontier_list, key=lambda Node: Node.function)

    def remove(self):
        return self.frontier_list.pop(0)

    def is_empty(self):
        return len(self.frontier_list) == 0
"""
