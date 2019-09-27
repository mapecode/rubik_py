import json


def read(path):
    with open(path, 'r') as file:
        return json.load(file)


def to_str(dic):
    s = ''

    for key, value in dic.items():
        for l in value:
            s += (''.join(str(i) for i in l))

    return s, len(l)


def to_string(cube_dict):
    values = str(cube_dict.values())
    s = ''
    for i in values:
        if i.isdigit():
            s += i
    return s





