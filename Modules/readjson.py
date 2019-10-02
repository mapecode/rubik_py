import json


def read_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def write_json(cube, path):
    pass
