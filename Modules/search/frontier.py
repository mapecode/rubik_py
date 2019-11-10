import bisect

"""
from queue import PriorityQueue

class Frontier:
    def __init__(self):
        self.__queue = PriorityQueue()

    def insert(self, node):
        self.__queue.put((node.function, node))

    def remove(self):
        return self.__queue.get()[1]

    def is_empty(self):
        return self.__queue.empty()

"""


class Frontier:
    def __init__(self):
        self.__frontier_list = []

    def insert(self, nodes):
        for node in nodes:
            self.__frontier_list.append(node)

        self.__frontier_list = sorted(self.__frontier_list, key=lambda Node: Node.function)

    def remove(self):
        return self.__frontier_list.pop(0)

    def is_empty(self):
        return len(self.__frontier_list) == 0
