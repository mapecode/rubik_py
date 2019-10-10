import Modules.constants as constant
import numpy as np
import copy
import hashlib


def encode(s):
    h = hashlib.md5(s.encode())
    return h.hexdigest()


def create_cube(cube_values):
    cube = []

    for v in cube_values:
        cube.append(np.array(v))

    return cube, len(cube[0])


def invert_sequence(sequence):
    sequence = sequence.swapcase()
    seq_invert = ''

    for i in range(len(sequence) - 1, -1, -2):
        seq_invert += sequence[i - 1] + sequence[i]

    return seq_invert


class Cube:
    def __init__(self, dic_cube):
        self.faces, self.n = create_cube(dic_cube.values())
        self.key = self.__cube_to_md5()

    def __cube_to_md5(self):
        s = ''
        for n in self.faces:
            s += (''.join(str(i) for i in n))

        return encode(s.replace('[', '').replace(']', '').replace(' ', ''))

    def __update_key(self):
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

    def apply_sequence(self, sequence):
        for i in range(0, len(sequence), 2):
            if (not sequence[i].lower() in ['l', 'd', 'b']) or (
                    int(sequence[i + 1]) < 0 or int(sequence[i + 1]) > self.n - 1):
                raise ValueError('Movimiento incorrecto: ', sequence[i] + sequence[i + 1])

            if sequence[i].lower() == 'l':
                self.__move_left(int(sequence[i + 1]), sequence[i].isupper())
            elif sequence[i].lower() == 'b':
                self.__move_back(int(sequence[i + 1]), sequence[i].isupper())
            elif sequence[i].lower() == 'd':
                self.__move_down(int(sequence[i + 1]), sequence[i].isupper())

        self.__update_key()

    def __rotate_face(self, rotate, id_face):
        """ Rotar una cara sobre si misma Generico"""
        if rotate:  # 90
            for i in range(3):  # Rotar 270 en numpy
                self.faces[id_face] = np.rot90(self.faces[id_face])
        else:  # -90
            self.faces[id_face] = np.rot90(self.faces[id_face])

    def __move_back(self, row, rotate):
        def rotate_row():
            """ Rotar fila """
            faces_sequence = [constant.DOWN, constant.RIGHT, constant.UP, constant.LEFT]  # Secuencia 90 grados
            if not rotate:  # -90 grados
                faces_sequence = faces_sequence[::-1]  # Inversa de la secuencia

            faces_copy = [copy.copy(self.faces[id_face][row]) for id_face in faces_sequence]

            for i in range(len(faces_sequence)):
                self.faces[faces_sequence[i]][row] = faces_copy[i - 1]

        # Comprobacion rotacion sobre si misma (BACK o FRONT)
        if row == 0:
            self.__rotate_face(rotate, constant.BACK)
        elif row == self.n - 1:
            self.__rotate_face(rotate, constant.FRONT)

        rotate_row()

    def __move_left(self, column, rotate):
        def rotate_column():
            '''Rotar columna'''
            faces_sequence = [constant.FRONT, constant.DOWN, constant.BACK, constant.UP]  # Secuencia de 90 grados
            if not rotate:  # -90 grados
                faces_sequence = faces_sequence[::-1]  # Inversa de la secuencia

            faces_copy = []
            pos = self.n - (column + 1)
            for id_face in faces_sequence:
                if id_face == constant.UP:
                    faces_copy.append(copy.copy(self.faces[id_face][:, pos])[::-1])
                else:
                    faces_copy.append(copy.copy(self.faces[id_face][:, column]))

            for i in range(len(faces_sequence)):
                if faces_sequence[i] == constant.UP:
                    self.faces[faces_sequence[i]][:, pos] = faces_copy[i - 1][::-1]
                else:
                    self.faces[faces_sequence[i]][:, column] = faces_copy[i - 1]

        # Comprobacion rotacion sobre si misma (Left o Right)
        if column == 0:
            self.__rotate_face(rotate, constant.LEFT)
        elif column == self.n - 1:
            self.__rotate_face(rotate, constant.RIGHT)

        rotate_column()

    def __move_down(self, row_column, rotate):
        '''Rotar fila - columna'''

        def rotate_row_column():

            faces_sequence = [constant.BACK, constant.RIGHT, constant.FRONT, constant.LEFT]
            if not rotate:
                faces_sequence = faces_sequence[::-1]

            faces_copy = []
            pos = self.n - (row_column + 1)

            for id_face in faces_sequence:
                if id_face is constant.BACK:
                    faces_copy.append(copy.copy(self.faces[id_face][pos]))
                elif id_face is constant.RIGHT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, row_column])[::-1])
                elif id_face is constant.FRONT:
                    faces_copy.append(copy.copy(self.faces[id_face][row_column]))
                elif id_face is constant.LEFT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, pos])[::-1])

            for i in range(len(faces_sequence)):
                if faces_sequence[i] is constant.BACK:
                    self.faces[faces_sequence[i]][pos] = faces_copy[i - 1]
                elif faces_sequence[i] is constant.RIGHT:
                    self.faces[faces_sequence[i]][:, row_column] = faces_copy[i - 1][::-1]
                elif faces_sequence[i] is constant.FRONT:
                    self.faces[faces_sequence[i]][row_column] = faces_copy[i - 1]
                elif faces_sequence[i] is constant.LEFT:
                    self.faces[faces_sequence[i]][:, pos] = faces_copy[i - 1][::-1]

        # Comprobacion rotacion sobre si misma (Down o Up)
        if row_column == 0:
            self.__rotate_face(rotate, constant.DOWN)
        elif row_column == self.n - 1:
            self.__rotate_face(rotate, constant.UP)

        rotate_row_column()
