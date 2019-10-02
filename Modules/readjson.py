import json


def read(path):
    with open(path, 'r') as file:
        return json.load(file)

def json_to_cube():
    pass

def to_str(dic):
    s = ''
    for key, value in dic.items():
        for l in value:
            s += (''.join(str(i) for i in l))
    return s
