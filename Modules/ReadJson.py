#!/usr/bin/env pyhton3
# -*- coding: utf-8 -*-

import json

with open('Files/cube3x3.json', 'r') as file:
    initState = file.read()

cube = json.loads(initState)
print(cube)
print(json.dumps(cube,indent=4))                    # Dar identacion a la hora de mostrar por pantalla el json