import json


def read(path):
    with open(path, 'r') as file:
        return json.load(file)
