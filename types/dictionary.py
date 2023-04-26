'''
dict() - Словарь -> упорядоченна коллекция элементов (python 3.7 -> ordered). Каждый элемент внутри словаря хранится ввиде пары: {ключ: знечение}

Ассоциативный массив, hash table, object(js), structure == dictionary(property)

Ключами могут быть только неизменяемые типы данных и в словаре сохраняются уникальные ключи.
Тогда как значениями могут выступать любые типы данных и значения могут повторться.

'''

'''
dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.

'''

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }

# print(thisdict)
# print(type(thisdict))
# print(thisdict['brand'], thisdict['model'])
# print(thisdict['year'])

# thisdict['motor'] = 'GTE Turbo'
# print(thisdict)
# thisdict['brand'] = 'Tesla'
# print(thisdict)
# thisdict['model'] = 'S'
# print(thisdict)

# множества
# a = set()
# a = {'a', 1, 1, 'b', 'c', 4, 6}

# print(a)

# Словари
# a = {}
# print(type(a))

# ---------------------------------------

# print(dir(dict))

# items, keys, values

# user_info = {
#     'fist_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',
# }

# ls = user_info.keys()
# ls = list(ls)
# print(ls[2:])

# ls = list(user_info.values())

# print(ls)

# items = user_info.items()
# print(items)

# print(user_info)
# for value in user_info.values():
#     print(value)

# for key in user_info.keys():
#     print(key)

# for x in user_info.items():
#     print(f'key: {x[0]}, values: {x[1]}')

# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, values: {value}')


# Изменение в словаре
# dict_ = {'name': 'Jack', 'age': 17}
# print(dict_)
# dict_['name'] = 'John'
# dict_['age'] = 24
# dict_['address'] = 'WinterFell'
# print(dict_)
# dict_.update({'age': 25, 'address': 'BlackCastle'})
# print(dict_)


#---------------------------------------------------
# Получение данных со словаря

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_[2], '!!!')
# print(dict_.get(1))

# setdefault - работает также как get, но если нет такого ключа, то он создает новую пару из этого ключа

# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.setdefault(5, 'Manty'))
# print(dict_)

#--------------------------------------------
# Создание словаря - fromkeys
# ls = list(range(1, 100))
# new_dict = dict.fromkeys(ls, 'value')
# print(new_dict)

#-------------------------------------------
# Удаление элементов

# pop(), popitem()

# pop(<key>) - удфляет пару по ключю

# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.pop('last_name') # не существующий ключ возвратит ошибку
# print(dict_)
# print(removed)

# popitem() - возвращает последнюю пару
# dict_ = {'name': 'John', 'last_name': 'Snow'}
# print(dict_)
# removed = dict_.popitem()
# print(dict_)
# print(removed)

#--------------------------------------------

'''
roles = {
    0: 'Admin',
    1: 'Customer',
    2: 'Vendor',
}

users = {
    55: {
    'id': 55, 'role': roles[2], 'username': 'Tirion',
    },
    2:{
    'id': 2, 'role': roles[0], 'username': 'John Snow',
    },
    3:{
    'id': 3, 'role': roles[1], 'username': 'Raychel'
    }
}
print(users)

product = {
    'id': 1, 
    'title': 'Samsung Galaxy A51',
    'description': 'Lorem Ipsum',
    'price': 250,
}

print(product)
id_user = int(input('Vvedite id: '))

if users[id_user]['role'] == roles[0]:
    product['description'] = input('Vvedita opisanie')
else:
    print('You do not have permissions!')

print(product)

'''




ls = [1,2,3,4,5,6]
ls1 = ['red', 'blue', 'green', 'black', 'pink', 'white']

a1 = dict(zip(ls, ls1))
a2 = {'name': 1}
a3 = {k:k*2 for k in range(1, 11)}

print(a1, a2, a3)










