# JSON - JavaScript Object Notation 
# Это единый тескстовый формат данных, был создан для хранения и передачи данных между сервисами.

# <filename>.json # фал в формате JSON
# {
#     "id": 1,
#     "author": {
#         "name": "Ed Shiron",
#         "age": 35
#     },
#     "title": "don't",
#     "feat": false
# }
# } ---  это JSON


# !!!!!
# js object == {key: value}
# Py dict == {key: value}
# JSON == {key: value}

# Процессы Сериальзации и Десериализации данных (конвертация)

# Сериальзация (запись данных в JSON) - это перевод из Python в JSON формат

# dump - записывает данные в файл формата JSON
# dumps - записывает данные в текст формата JSON


# Десериальзация (чтение данных из JSON) - это процесс перевода из JSON в Python Dict формат

# load - функция, которая считывает данные из файла JSON
# loads - функция, которая считывает данные из текста JSON


# ----------------------------------------------------

# Процесс сериализации

import json

# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# print(dict_, type(dict_))

# json_text = json.dumps(dict_)
# print()
# print(json_text, type(json_text))


# dict_ = {
#     'name': 'John Snow',
#     'age': 24,
#     'status': True,
#     'wife': False,
#     'children': None
# }

# with open('new.json', 'w') as file:
#     json.dump(dict_, file, indent=4)


# -------------------------------------

# процесс десериальзации
# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()

# print(json_data, type(json_data))

# dict_ = json.loads(json_data)
# print(dict_)


# import json

# with open('new.json', 'r') as file:
#     dict_ = json.load(file)
#     print(dict_, type(dict_))


# from urllib.request import urlopen
# import json
# import pprint as pp

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)
# # print(json_data, dir(json_data))

# dict_ = json.load(json_data)
# pp.pprint(dict_)











