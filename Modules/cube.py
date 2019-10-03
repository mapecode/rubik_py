import Modules.constants as constant
import Modules.cipher as cipher
import numpy as np
import copy


def create_cube(cube_values):
    cube = []

    for v in cube_values:
        cube.append(np.array(v))

    return cube, len(cube[0])


class Cube:
    def __init__(self, dic_cube):
        self.faces, self.n = create_cube(dic_cube.values())
        self.key = self.__cube_to_md5()

    def __cube_to_md5(self):
        s = ''
        for n in self.faces:
            s += (''.join(str(i) for i in n))

        return cipher.encode(s.replace('[', '').replace(']', '').replace(' ', ''))

    def update_key(self):
        self.key = self.__cube_to_md5()

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
            sequence = [constant.DOWN, constant.RIGHT, constant.UP, constant.LEFT]  # Secuencia 90 grados
            if not rotate:  # -90
                sequence = sequence[::-1]  # Inversa de la secuencia

            faces_copy = [copy.copy(self.faces[id_face][row]) for id_face in sequence]

            for i in range(len(sequence)):
                self.faces[sequence[i]][row] = faces_copy[i - 1]

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
                back = copy.copy(self.faces[constant.BACK][:, column])  # Valor inicial de back [:,column]
                self.faces[constant.BACK][:, column] = down
                # Rotar back to up
                up = copy.copy(self.faces[constant.UP][:, self.n - (column + 1)])  # Valor inicial up
                self.faces[constant.UP][:, self.n - (column + 1)] = back[::-1]  # Invertimos columna back to up
                # Rotar up to front
                self.faces[constant.FRONT][:, column] = up[::-1]
            else:  # -90
                # Rotar front to up
                front = copy.copy(self.faces[constant.FRONT][:, column])  # Valor inicial de front[:, column]
                up = copy.copy(self.faces[constant.UP][:, self.n - (column + 1)])  # Valor incial de up[:, column]
                self.faces[constant.UP][:, self.n - (column + 1)] = front[::-1]  # Invertimos columna front to up
                # Rotar up to back
                back = copy.copy(self.faces[constant.BACK][:, column])  # Valor inicial de back[:, column]
                self.faces[constant.BACK][:, column] = up[::-1]  # Invertimos columna up to back
                # Rotar back to down
                down = copy.copy(self.faces[constant.DOWN][:, column])  # Valor incial de down[:, column]
                self.faces[constant.DOWN][:, column] = back
                # Rotar down to front
                self.faces[constant.FRONT][:, column] = down

        # Comprobacion rotacion sobre si misma (Left o Right)
        if column == 0:
            self.rotate_face(rotate, constant.LEFT)
        elif column == self.n - 1:
            self.rotate_face(rotate, constant.RIGHT)

        rotate_column()

    def move_down(self, row_column, rotate):
        def rotate_rc():
            sequence = [constant.BACK, constant.RIGHT, constant.FRONT, constant.LEFT]
            if not rotate:
                sequence = sequence[::-1]

            faces_copy = []
            pos = self.n - (row_column + 1)

            for id_face in sequence:
                if id_face is constant.BACK:
                    faces_copy.append(copy.copy(self.faces[id_face][pos]))
                elif id_face is constant.RIGHT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, row_column])[::-1])
                elif id_face is constant.FRONT:
                    faces_copy.append(copy.copy(self.faces[id_face][row_column]))
                elif id_face is constant.LEFT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, pos])[::-1])

            for i in range(len(sequence)):
                if sequence[i] is constant.BACK:
                    self.faces[sequence[i]][pos] = faces_copy[i - 1]
                elif sequence[i] is constant.RIGHT:
                    self.faces[sequence[i]][:, row_column] = faces_copy[i - 1]
                elif sequence[i] is constant.FRONT:
                    self.faces[sequence[i]][row_column] = faces_copy[i - 1]
                elif sequence[i] is constant.LEFT:
                    self.faces[sequence[i]][:, pos] = faces_copy[i - 1]


        # Comprobacion rotacion sobre si misma (Down o Up)
        if row_column == 0:
            self.rotate_face(rotate, constant.DOWN)
        elif row_column == self.n - 1:
            self.rotate_face(rotate, constant.UP)

        rotate_rc()
