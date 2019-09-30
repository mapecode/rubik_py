import Modules.constants as constant
import numpy as np
import copy


class Cube:
    def __init__(self, id_string, n):
        self.id_string = id_string
        self.n = n
        self.faces = self.__create_cube()
        self.__faces_init = tuple(self.faces)

    # Creacion del cubo
    def __create_cube(self):
        faces = []
        i = 0

        while i < constant.N_FACES:
            faces.append(self.__create_face(i))
            i += 1
        return faces

    # Crear las caras del cubo
    def __create_face(self, n_face):
        start = n_face * self.n * self.n
        end = start + self.n * self.n - 1
        i = start
        face = []

        while i <= end:
            face.append(self.__create_row(i, i + self.n))
            i += self.n

        return np.array(face)

    # Creacion de las filas
    def __create_row(self, start, end):
        row = []

        while start < end:
            row.append(int(self.id_string[start]))
            start += 1

        return row

    def __face_str(self, n_face):
        s = ''

        for row in self.faces[n_face]:
            s += str(row) + '\n'

        return s

    def __str__(self):
        s = ''
        for row in self.faces[constant.BACK]:
            s += str(row) + '\n'

        s+='\n'

        for i in range(self.n):
            s += str(self.faces[constant.LEFT][i]) + ' ' + str(self.faces[constant.DOWN][i]) + ' ' + \
                 str(self.faces[constant.RIGHT][i]) + ' ' + str(self.faces[constant.UP][i]) + '\n'


        s += '\n'

        for row in self.faces[constant.FRONT]:
            s += str(row) + '\n'

        s+=self.n*'-------------------------'+'\n'


        return s

        # MOVIMIENTOS

    """ DEFINICION DE MOVIMIENTO
    row: fila que se mueve
        0,1,2
    rotate: 
        True: 90
        False: -90
    """

    def move_back(self, row, rotate):
        def rot_right():
            """ Rotar fila 90 grados"""
            # Rotar left to down (down[row] = left[row])
            down = copy.copy(self.faces[constant.DOWN][row])  # Valor inicial de down[row]
            self.faces[constant.DOWN][row] = self.faces[constant.LEFT][row]
            # Rotar down to right (right[row] = down[row])
            right = copy.copy(self.faces[constant.RIGHT][row])  # Valor inicial de right[row]
            self.faces[constant.RIGHT][row] = down
            # Rotar right to up (up[row] = right[row])
            up = copy.copy(self.faces[constant.UP][row])  # Valor inicial de up[row]
            self.faces[constant.RIGHT][row] = right
            # Rotar up to left (left[0] = up[0])
            self.faces[constant.LEFT][row] = up

        def rot_left():
            """ Rotar fila -90 grados"""
            pass

        if row == 0:  # Rotar cara back y fila 0
            if rotate:  # 90 (derecha)
                # Rotar back
                for i in range(3):  # Rotar 270 en numpy
                    self.faces[constant.BACK] = np.rot90(self.faces[constant.BACK])
                rot_right()
            else:  # -90 (izquierda)
                # Rotar back
                self.faces[constant.BACK] = np.rot90(self.faces[constant.BACK])
                rot_left()
        elif row == 1:  # Rotar fila 1
            if rotate:  # 90 (derecha)
                rot_right()
            else:  # -90 (izquierda)
                rot_left()
        elif row == 2:  # Rotar cara front y fila 2
            if rotate:  # 90 (derecha)
                # Rotar front
                for i in range(3):  # Rotar 270 en numpy
                    self.faces[constant.FRONT] = np.rot90(self.faces[constant.FRONT])
                rot_right()
            else:  # -90 (izquierda)
                self.faces[constant.FRONT] = np.rot90(self.faces[constant.FRONT])
                rot_left()
