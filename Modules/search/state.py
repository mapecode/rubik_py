from Modules.cube import Cube
from Modules.json import read_json


class State:
    def __init__(self, path):
        self.cube = Cube(read_json(path))

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

    def is_correct(self):
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
            for i in range(1, self.cube.n * 2):
                # Compara el primer valor con el resto de valores
                if face[0][0] != face[i // self.cube.n][i % self.cube.n]:
                    return False
            return True

        correct = True
        for face in self.cube.faces:
            correct = is_face_correct(face)

            if not correct:
                break

        return correct
