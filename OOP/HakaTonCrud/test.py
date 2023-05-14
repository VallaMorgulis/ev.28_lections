import json

with open('data.json', 'r') as file:
    python_obj = json.load(file)
    # dict_obj = {x for x in python_obj}

print(python_obj)