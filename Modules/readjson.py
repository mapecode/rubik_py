import json



def read(path):
    with open(path, 'r') as file:
        return json.load(file)

def to_string(cube_dict):
    values = str(cube_dict.values())
    s = ''
    for i in values:
        if i.isdigit():
            s += i
    return s





print(to_string(read("../Files/cube3x3.json")))




