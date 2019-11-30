from Modules.cube import Cube
import math
import numpy as np


class State:
    def __init__(self, dic_cube):
        self.cube = Cube(dic_cube)

    def apply_action(self, action):
        """
        Comprueba si el movimiento es correcto y lo aplica al cubo del estado.
        Si el movimiento se aplica se actualiza el identificador del cubo.
        :param action: movimiento a realizar
        """
        if (not action[0].lower() in ['l', 'd', 'b']) or (
                int(action[1]) < 0 or int(action[1]) > self.cube.n - 1):
            raise ValueError('Movimiento incorrecto: ', action)

        if action[0].lower() == 'l':
            self.cube.move_left(int(action[1]), action[0].isupper())
        elif action[0].lower() == 'b':
            self.cube.move_back(int(action[1]), action[0].isupper())
        elif action[0].lower() == 'd':
            self.cube.move_down(int(action[1]), action[0].isupper())

        self.cube.update_key()

    def is_correct(self, strategy, heuristic=None):
        """
        Comprueba si el cubo esta perfectamente formado
        :return: comprobacion
        """

        def is_face_correct(face):
            """
            Comprueba si una cara es correcta, es decir, los valores iguales.
            :param face: cara a comprobar
            :return: comprobacion
            """
            for i in range(1, self.cube.n * self.cube.n):
                # Compara el primer valor con el resto de valores
                if face[0][0] != face[i // self.cube.n][i % self.cube.n]:
                    return False
            return True

        if heuristic is not None:
            return heuristic == 0
        else:
            correct = True
            for face in self.cube.faces:
                correct = is_face_correct(face)

                if not correct:
                    break

            return correct

    def calculate_heuristic(self):
        def count_colors(f):
            counter = np.zeros((6,), dtype=int)

            for i in range(0, self.cube.n * self.cube.n):
                counter[f[i // self.cube.n][i % self.cube.n]] += 1

            return counter

        def calculate_entropy(c):
            entropy = 0
            for i in range(0, 6):
                if c[i] > 0:
                    p = c[i] / (self.cube.n * self.cube.n)
                    entropy += p * math.log(p, 6)

            return -entropy

        heuristic = 0
        for face in self.cube.faces:
            counter = count_colors(face)
            heuristic += calculate_entropy(counter)

        return round(heuristic, 2)
