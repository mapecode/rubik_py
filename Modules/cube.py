import Modules.constants as constant


class Cube:
    def __init__(self, id_string, n):
        self.id_string = id_string
        self.n = n
        self.faces = self.__create_cube()

    #Creacion del cubo
    def __create_cube(self):
        faces = []
        i = 0

        while i < constant.N_FACES:
            faces.append(self.__create_face(i))
            i += 1
        return faces

    #Crear las caras del cubo
    def __create_face(self, n_face):
        start = n_face * self.n * self.n
        end = start + self.n * self.n - 1
        i = start
        face = []

        while i <= end:
            face.append(self.__create_row(i, i + self.n))
            i += self.n

        return face

    #Creacion de las filas
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

    def move_back(self):
        if
