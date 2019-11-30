import Modules.constants as constant
import numpy as np
import copy
import hashlib


def encode(s):
    """
    Genera el identificador (hash) resultante de la codificacion del cubo, mediante la codificacion "md5"
    (perteneciente a la libreria hashlib).
    :param s: cadena que corresponde a una representacion del estado del cubo
    :return: identificador del cubo en hexadecimal (hash)
    """

    h = hashlib.md5(s.encode())
    return h.hexdigest()


def create_cube(cube_values):
    """
    Creacion del cubo mediante los valores existentes en el diccionario (KEY: Cara cubo, VALUES: valores de dicha cara)
    generado resultado del fichero JSON.
    :param cube_values: Compuesto por los valores de cada una de las caras que forman el cubo.
    :return: el cubo en formato de lista y la dimension de una cara del cubo (dado que es un cubo de N x N).
    """

    cube = []
    for v in cube_values:
        cube.append(np.array(v))

    return cube, len(cube[0])


class Cube:
    def __init__(self, dict_cube):
        """
        Metodo constructor de la clase "Cube"
        :param dict_cube: Diccionario donde se almacena la informacion del cubo, generado a partir del fichero JSON.
        """

        self.faces, self.n = create_cube(dict_cube.values())
        self.hash = self.__cube_to_md5()

    def __cube_to_md5(self):
        """
        Generar identificador (hash) del cubo, para ello se llama al metodo encode().
        :return: identificador del cubo en el estado actual.
        """

        s = ''
        for n in self.faces:
            s += (''.join(str(i) for i in n))

        return encode(s.replace('[', '').replace(']', '').replace(' ', ''))

    def update_key(self):
        """
        Actualizacion del identficador (hash) del cubo, utilizado a la hora de la generacion nuevos estados.
        :return: Nuevo identificador (hash) del cubo, perteneciente a un estado distinto al estado inicial.
        """

        self.hash = self.__cube_to_md5()

    def __str__(self):
        """
        Representacion del objeto, mediante el paso de sus atributos a String.
        Asi cuando querramos imprimir el objeto por pantalla el programa llamara por defecto a dicho metodo "__str__".
        :return: Un String con la representacion del cubo.
        """

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

    def __rotate_face(self, rotate, id_face):
        """
        Rotacion de una cara del cubo sobre si misma (a derecha 90º, a izquierda -90º).
        :param rotate: indica la direccion de rotacion:
                - Si "rotate" es True: Rotar 90º.
                - Si "rotate" es False: Rotar -90º.
        :param id_face: Representa el ID de la cara a rotar.
                Este ID esta representado mediante una serie de 6 constantes:
                    * BACK = 0
                    * DOWN = 1
                    * FRONT = 2
                    * LEFT = 3
                    * RIGHT = 4
                    * UP = 5
        """

        if rotate:  # 90
            for i in range(3):  # Rotar 270 en numpy
                self.faces[id_face] = np.rot90(self.faces[id_face])
        else:  # -90
            self.faces[id_face] = np.rot90(self.faces[id_face])

    def move_back(self, row, rotate):
        """
        Realizar movimiento BACK.
        :param row: Indica el numero de fila a rotar, mediante un entero perteneciente al rango (0 <= row < N),
                    siendo "N" la dimension del cubo.
        :param rotate: Variable booleana, que indica la rotacion del cubo:
                        * True --> 90º
                        * False --> - 90º
        """

        def rotate_row():
            """
            Rotacion de fila, se rotaran las filas correspondientes a la accion del movimiento BACK.
            Para ello es necesario saber el orden de rotatacion de las filas, para ello se ha generado una secuencia de caras.
                * Si se realiza una rotacion de 90º (rotate == True) se aplica la secuencia.
                * Si se realiza una rotacion de - 90º (rotate == False), se aplica la inversa de la secuencia.
            """

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

    def move_left(self, column, rotate):
        """
        Realizar movimiento LEFT.
        :param column: Indica el numero de columna a rotar, mediante un entero perteneciente al rango (0 <= column < N),
                    siendo "N" la dimension del cubo.
        :param rotate: Variable booleana, que indica la rotacion del cubo:
                        * True --> 90º
                        * False --> - 90º
        """

        def rotate_column():
            """
            Rotacion de columna, se rotaran las columna correspondientes a la accion del movimiento LEFT.
            Para ello es necesario saber el orden de rotatacion de las columnas, para ello se ha generado una secuencia de caras.
                * Si se realiza una rotacion de 90º (rotate == True) se aplica la secuencia.
                * Si se realiza una rotacion de - 90º (rotate == False), se aplica la inversa de la secuencia.
            """

            faces_sequence = [constant.FRONT, constant.DOWN, constant.BACK, constant.UP]  # Secuencia de 90 grados
            if not rotate:  # -90 grados
                faces_sequence = faces_sequence[::-1]  # Inversa de la secuencia

            faces_copy = []
            pos = self.n - (column + 1)
            for id_face in faces_sequence:
                if id_face is constant.UP:
                    faces_copy.append(copy.copy(self.faces[id_face][:, pos])[::-1])
                else:
                    faces_copy.append(copy.copy(self.faces[id_face][:, column]))

            for i in range(len(faces_sequence)):
                if faces_sequence[i] is constant.UP:
                    self.faces[faces_sequence[i]][:, pos] = faces_copy[i - 1][::-1]
                else:
                    self.faces[faces_sequence[i]][:, column] = faces_copy[i - 1]

        # Comprobacion rotacion sobre si misma (Left o Right)
        if column == 0:
            self.__rotate_face(rotate, constant.LEFT)
        elif column == self.n - 1:
            self.__rotate_face(rotate, constant.RIGHT)

        rotate_column()

    def move_down(self, row_column, rotate):
        """
        Realizar movimiento DOWN.
        :param row_column: Indica el numero de columna o fila a rotar, mediante un entero perteneciente al rango (0 <= row_column < N).
                            Al tratarse de un cubo de dimensiones N x N, el valor de la fila y la columna es el mismo).
        :param rotate: Variable booleana, que indica la rotacion del cubo:
                        * True --> 90º
                        * False --> - 90º
        """

        def rotate_row_column():
            """
            Rotacion de columna, se rotaran las columna correspondientes a la accion del movimiento LEFT.
            Para ello es necesario saber el orden de rotatacion de las columnas, para ello se ha generado una secuencia de caras.
                * Si se realiza una rotacion de 90º (rotate == True) se aplica la secuencia.
                * Si se realiza una rotacion de - 90º (rotate == False), se aplica la inversa de la secuencia.
            """

            faces_sequence = [constant.BACK, constant.RIGHT, constant.FRONT, constant.LEFT]
            if not rotate:
                faces_sequence = faces_sequence[::-1]

            faces_copy = []
            pos = self.n - (row_column + 1)

            for id_face in faces_sequence:
                if id_face is constant.BACK:
                    faces_copy.append(copy.copy(self.faces[id_face][pos]))
                elif id_face is constant.RIGHT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, row_column]))
                elif id_face is constant.FRONT:
                    faces_copy.append(copy.copy(self.faces[id_face][row_column]))
                elif id_face is constant.LEFT:
                    faces_copy.append(copy.copy(self.faces[id_face][:, pos]))

            for i in range(len(faces_sequence)):
                if faces_sequence[i] is constant.BACK:
                    if rotate:
                        self.faces[faces_sequence[i]][pos] = faces_copy[i - 1][::-1]
                    else:
                        self.faces[faces_sequence[i]][pos] = faces_copy[i - 1]
                elif faces_sequence[i] is constant.RIGHT:
                    if rotate:
                        self.faces[faces_sequence[i]][:, row_column] = faces_copy[i - 1]
                    else:
                        self.faces[faces_sequence[i]][:, row_column] = faces_copy[i - 1][::-1]
                elif faces_sequence[i] is constant.FRONT:
                    if rotate:
                        self.faces[faces_sequence[i]][row_column] = faces_copy[i - 1][::-1]
                    else:
                        self.faces[faces_sequence[i]][row_column] = faces_copy[i - 1]

                elif faces_sequence[i] is constant.LEFT:
                    if rotate:
                        self.faces[faces_sequence[i]][:, pos] = faces_copy[i - 1]
                    else:
                        self.faces[faces_sequence[i]][:, pos] = faces_copy[i - 1][::-1]

        # Comprobacion rotacion sobre si misma (Down o Up)
        if row_column == 0:
            self.__rotate_face(rotate, constant.DOWN)
        elif row_column == self.n - 1:
            self.__rotate_face(rotate, constant.UP)

        rotate_row_column()
