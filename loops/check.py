# task 1

# clients = {'Myrat': 24, 'Erzhan': 21, 'Karina': 24, 'Altynay': 17, 'Aibek': 16}

# user = input('Vvedite imya: ')

# for k, v in clients.items():
#     if user == k:
#         if v <= 17:
#             print(f'{k} вам рано посещать клуб')
#         else:
#             print(f'{k} вам можно пройти в клуб')

# Task 2
# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {}

# for k, v in a.items():
#     for k2, v2 in v.items():
#         b[k] = v2

# print(b)

# task 3

# a = {'apple': 12, 'orange': 43, 'pinapple': 35, 'dragon friut': 24}

# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)

# print(a)

# task 4

# a = {'apple': 12, 'orange': 43, 'pinapple': 35, 'dragon friut': 24}
# b = 0
# for k,v in a.items():
#     b = b + v

# print(b)


# task 5

# a = {}
# for i in range(1, 11):
#     a.setdefault(i, pow(i, 2))

# print(a)

# task 6

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# b = {}

# for k, v in my_dict.items():
#     for k2, v2 in v.items():
#         b[k] = v2

# print(b)

# task 7

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values()) 
# sorted_dict = {}
# for i in sorted_values: 
#     for k in dict_.keys(): 
#          if dict_[k] == i: 
#             sorted_dict[k] = dict_[k] 
#             break 

# print(sorted_dict)


# task 8

# sum = int(input('Введите сумму, которая у Вас сейчас есть в бумажнике: '))
# if sum < 0:
#     print('Сумма не может быть отрицательной!')
