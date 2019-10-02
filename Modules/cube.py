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
        self.cube_md5 = self.__cube_to_md5()

    def __cube_to_md5(self):
        s = ''
        for n in self.faces[0]:
            s += (''.join(str(i) for i in n))

        return cipher.encode(s)


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

    def move_down(self, column, rotate):
        def rotate():
            pass
