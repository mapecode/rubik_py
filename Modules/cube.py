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
        return f"BACK\n{self.__face_str(constant.BACK)}\n" \
               f"DOWN\n{self.__face_str(constant.DOWN)}\n" \
               f"FRONT\n{self.__face_str(constant.FRONT)}\n" \
               f"LEFT\n{self.__face_str(constant.LEFT)}\n" \
               f"RIGHT\n{self.__face_str(constant.RIGHT)}\n" \
               f"UP\n{self.__face_str(constant.UP)}\n" \
 \
            # MOVIMIENTOS

    """ DEFINICION DE MOVIMIENTO
    row: fila que se mueve
        0,1,2
    rotate: 
        True: 90
        False: -90
    """

    def move_back(self, row, rotate):
        if row == 0:
            if rotate:  # 90 (derecha)
                # Rotar cara principal
                for i in range(3):  # Rotar 270 en numpy
                    self.faces[constant.BACK] = np.rot90(self.faces[constant.BACK])
                # Rotar left to down (down[0] = left[0])
                down = copy.copy(self.faces[constant.DOWN][0])  # Valor inicial de down[0]
                self.faces[constant.DOWN][row] = self.faces[constant.LEFT][row]
                # Rotar down to right (right[0] = down[0])
                right = copy.copy(self.faces[constant.RIGHT][0])  # Valor inicial de right[0]
                self.faces[constant.RIGHT][row] = down
                # Rotar right to up (up[0] = right[0])
                up = copy.copy(self.faces[constant.UP][0])  # Valor inicial de up[0]
                self.faces[constant.RIGHT][row] = right
                # Rotar up to left (left[0] = up[0])
                self.faces[constant.LEFT][row] = up
            else:  # -90 (izquierda)
                # Rotar cara principal
                self.faces[constant.BACK] = np.rot90(self.faces[constant.BACK])
        elif row == 1:
            pass
        elif row == 2:
            pass
