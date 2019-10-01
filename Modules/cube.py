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

        s += '\n'

        for i in range(self.n):
            s += str(self.faces[constant.LEFT][i]) + ' ' + str(self.faces[constant.DOWN][i]) + ' ' + \
                 str(self.faces[constant.RIGHT][i]) + ' ' + str(self.faces[constant.UP][i]) + '\n'

        s += '\n'

        for row in self.faces[constant.FRONT]:
            s += str(row) + '\n'

        s += self.n * '-------------------------' + '\n'

        return s

        # MOVIMIENTOS

    """ DEFINICION DE MOVIMIENTO
    row: fila que se mueve
        0,1,2
    rotate: 
        True: 90
        False: -90
    """

    def rotate_face(self, rotate, id_face):
        """ Rotar una cara sobre si misma Generico"""
        if rotate:  # 90
            for i in range(3):  # Rotar 270 en numpy
                self.faces[id_face] = np.rot90(self.faces[id_face])
        else:  # -90
            self.faces[id_face] = np.rot90(self.faces[id_face])

    def move_back(self, row, rotate):
        def rotate_row():
            """ Rotar filas """
            if rotate:  # 90
                # Rotar left to down (down[row] = left[row])
                left = copy.copy(self.faces[constant.LEFT][row])  # Valor inicial de left[row]
                down = copy.copy(self.faces[constant.DOWN][row])  # Valor inicial de down[row]
                self.faces[constant.DOWN][row] = left
                # Rotar down to right (right[row] = down[row])
                right = copy.copy(self.faces[constant.RIGHT][row])  # Valor inicial de right[row]
                self.faces[constant.RIGHT][row] = down
                # Rotar right to up (up[row] = right[row])
                up = copy.copy(self.faces[constant.UP][row])  # Valor inicial de up[row]
                self.faces[constant.UP][row] = right
                # Rotar up to left (left[row] = up[row])
                self.faces[constant.LEFT][row] = up
            else:  # -90
                # Rotar left to up (up[row] = left[row])
                left = copy.copy(self.faces[constant.LEFT][row])  # Valor inicial de left[row]
                up = copy.copy(self.faces[constant.UP][row])  # Valor inicial de up[row]
                self.faces[constant.UP][row] = left
                # Rotar up to right (right[row] = up[row])
                right = copy.copy(self.faces[constant.RIGHT][row])  # Valor inicial de right[row]
                self.faces[constant.RIGHT][row] = up
                # Rotar right to down (down[row] = right[row])
                down = copy.copy(self.faces[constant.DOWN][row])
                self.faces[constant.DOWN][row] = right
                # Rotar down to left (left[row] = down[row])
                self.faces[constant.LEFT][row] = down
        # Comprobacion rotacion sobre si misma (BACK o FRONT)
        if row == 0:
            self.rotate_face(rotate, constant.BACK)
        elif row == self.n - 1:
            self.rotate_face(rotate, constant.FRONT)

        rotate_row()

    def move_left(self, column, rotate):
        def rotate_column():
            '''Rotar columnas'''
            if rotate:
                # Rotar front to down (down[:, column] = front[:, column])
                front = copy.copy(self.faces[constant.FRONT][:, column])  # Valor incial de front[:, column]
                down = copy.copy(self.faces[constant.DOWN][:, column])  # Valor incial de down[:, column]
                self.faces[constant.DOWN][:, column] = front
                # Rotar down to back (back[:,column] = down[:, colummn])
                back = copy.copy(self.faces[constant.BACK][:, column])  # Valor incial de back [:,column]
                self.faces[constant.BACK][:, column] = down  # Invertimos columna down to back
                # Rotar back to up
                up = copy.copy(self.faces[constant.UP][:, self.n - (column + 1)])
                self.faces[constant.UP][:, self.n - (column + 1)] = back[::-1]  # Invertimos columna back to up
                # Rotar up to front
                self.faces[constant.FRONT][:, column] = up[::-1]
            else:  # -90
                # Rotar front to up
                front = copy.copy(self.faces[constant.FRONT][:, column])  # Valor incial de front[:, column]
                up = copy.copy(self.faces[constant.UP][:, self.n - (column + 1)])  # Valor incial de up[:, column]
                self.faces[constant.UP][:, self.n - (column + 1)] = front[::-1]
                # Rotar up to back
                back = copy.copy(self.faces[constant.BACK][:, self.n - (column + 1)])  # Valor incial de back[:, column]
                self.faces[constant.BACK][:, self.n - (column + 1)] = up[::-1]  # Invertimos columna up to back
                # Rotar back to down
                down = copy.copy(self.faces[constant.DOWN][:, column])  # Valor incial de down[:, column]
                self.faces[constant.DOWN][:, column] = back[::-1]  # Invertimos columna back to down
                # Rotar down to front
                self.faces[constant.FRONT][:, column] = down
        # Comprobacion cara a rotar sobre si misma (Left o Right)
        if column == 0:
            self.rotate_face(rotate, constant.LEFT)
        elif column == self.n - 1:
            self.rotate_face(rotate, constant.RIGHT)

        rotate_column()

    def move_down(self, column, rotate):
        def rotate():
            pass
