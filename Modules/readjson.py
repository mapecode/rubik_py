import json


def read(path):
    with open(path, 'r') as file:
        return json.load(file)


def to_str(dic):
    s = ''
    print(dic)
    for key, value in dic.items():
        for l in value:
            s += (''.join(str(i) for i in l))
    return s, len(l)
