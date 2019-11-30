import heapq


class Frontier:
    def __init__(self):
        """
        Constructor de la clase frontera, se crea una lista de forma privada que representara una
        cola de prioridad, gestionada con heapq
        """
        self.__queue = []

    def insert(self, nodes):
        """
        Inserta la lista de nodes segun la prioridad correspondiente, que depende de la f o id del nodo
        :param nodes: lista de nodos a introducir
        :return:
        """
        for node in nodes:
            heapq.heappush(self.__queue, node)

    def remove(self):
        """
        Devuelve y elimina el primer elemento de la frontera
        :return: primer elemento de self.__queue
        """
        return heapq.heappop(self.__queue)

    def is_empty(self):
        """
        Devuelve si la cola esta vacia
        :return: comprobacion de la longitud de self.__queue
        """
        return len(self.__queue) == 0
