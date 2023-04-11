
'''
Всторенные функции
'''

'''
Анонимная функция - lambda (Обычная функция с одной особенностью, у нее нет имени)
Принимает сколько угодно параметров, но всегда возвращает одно выражение
'''

# def hello():
#     return 'hello'

# print(hello())

# x = lambda: 'hello'
# print(x())

# x = lambda a, b, c: (a * b) % c
# print(x(5, 5, 5))



# x = lambda a, b, c=None: (a * b) ** c if c else a * b
# print(x(5, 5))

# def myFunc(n):
#     return lambda num: num * n

# my_doubler = myFunc(2)
# print(my_doubler(50))

# dict_ = {
#     'john': 500,
#     'tirion': 160_000,
#     'tom': 150,
#     'sanchar': 20,
#     'ayana': 100_000
# }

# new_dict = dict(sorted(dict_.items(), key=lambda x: x[1]), reversed=True)
# print(new_dict)

'''
map(function, iterable) - применяется к каждому элементу внутри iterble функцию, которую мы ей передаемв functions, закидывая в результат те данные, которые возвращает функция. В результате мы получаем mapoobject(iterator, в котором хранятся все наши данные.
'''

# ls = ['one', 'two', 'three', 'four']
# new_list = list(map(lambda x: x.capitalize(), ls))
# print(new_list)

# names = ['john', 'aria', 'baku', 'bakberdi', 'lilo']
# new_list = list(map(lambda x: f'hello,mr/mrs {x}', names))
# print(new_list)

'''
Функция высшего порядка - функция, которая принимает в качестве аргумента другую функцию
'''

# filter(function, iterable) - применяет ко всем элементам iterable функцию, которую мы передали и возвращает filterobject(итератор) только с теми элементами, для которых функция вернула True

# ls = ['johnSn', 'aria1', 'baku', 'bakberdi', 'lilo']
# res = list(filter(lambda x: len(x) > 4, ls))
# print(res)

'''
enumerate(iterable) - пронумеровывает каждый элемент внутри iterable ее собственным индексом
'''

# ls = ['johnSn', 'aria1', 'baku', 'bakberdi', 'lilo']
# new_list = list(enumerate(ls))
# print(new_list)

# new_list = {x: y for x, y in enumerate(ls)}
# print(new_list)

# zip(iterables) - она соединяет каждый элемент итеррируемых объектов между собой в тип данных tuple и возвразает итерратор.

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = dict(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500, 600]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip жля создания словарей
# d_keys = ['hostname', 'location', 'vendor', 'model', 'IP']
# data = {
#     'oktbr': ['bishkek_oktbr', 'Gorkaya 212', 'Vefa', 'Cisco', '10.255.0.12'],
#     '1may': ['bishkek_1may', 'Jibek-Jolu 212', 'Beli Dom', 'Cisco', '11.255.0.12'],
#     'svrdl': ['bishkek_svrdl', 'Ahunbaeva 212', 'Beli Dom', 'Cisco', '11.255.105.12']
# }

# bishkek_data = {}
# for k in data:
#     bishkek_data[k] = dict(zip(d_keys, data[k]))

# print(bishkek_data)

#------------------------------------------
# all(), any()

# all(Iterable) - возвращает True, если все элементы внутри итеррируемого объекта истина, иначе False

# ls = [5, 6, 7, []]
# print(all(ls))

# ip = '10.255.0.155'
# ip1 = '10.124.0y.202'

# result = all(x.isdigit() for x in ip1.split('.')) 
# print(result)


# any(Iterable) - возвращает True, если хотя бы один элементы внутри итеррируемого объекта истина, иначе False

# ls = [1, 3 [1, 2], 0]
# print(any(ls))

# ignore = ['rm -rf', 'sudo', 'reset', 'poweroff']
# command = input('Vvedite comandu: ')

# if any(x in command for x in ignore):
#     raise Exception('Block you!')
# print('It\'s OK')

# ПАРОЛЬ ГЕНЕРАТОР

# from random import choices
# from string import ascii_letters, digits
# from itertools import repeat

# symbols = '_()+-@!#%'
# q_pass = int(input('Vvedite kol-vo paroley: '))

# result = {
#     f(choices(ascii_letters, k=15), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of password: {len(result)}')
# from statistics import mean

# average = mean(len(x) for x in result)

# print(f'Avg len of pfasswords: {average}')



# CheckYouSelf

# 1

# def summa(x, y):
#     z = x + y
#     return z

# print(summa(2, 3))

# 2

# def istype(x, y):
#         return f'Тип данных {type(x)}, {type(y)}'

# print(istype(3, 'returt'))

# 3

# list_int = [1, 2, 3, 5, 67]
# def multipl(list_int):
#     from functools import reduce
#     res = reduce(lambda x, y: x * y, list_int)
#     return res

# print(multipl(list_int))

# 4

# def sound_letters(str_):
#     g = 0
#     s = 0
#     o = 0
#     for i in str_:
#         if i in 'уеыаоэяию':
#             g += 1
#         elif i in 'ёйцкнгшщзхъфвпрлджчсмтьб':
#             s += 1
#         else:
#             o += 1
#     return f'Гласных:  {g} Согласных: {s} Других символов: {o} '

# print(sound_letters('Привет артист! Как дале то?'))

# 5

# list_names = ['John', 'Vladislav', 'Timur']
# def multipl(list_names):
#     from functools import reduce
#     res = reduce(lambda x, y: x if (len(x) > len(y)) else y, list_names)
#     return res

# print(multipl(list_names))

# 6

# num = 3

# def mul(x):
#     global num
#     num = num ** 2
#     return num

# print(mul(num))
# print(mul(num))
# print(mul(num))

# 7

# matr = 10

# def size_matr():
#     matr2 = 5
   
#     def size_matr2():
#         matr3 = 3

#         return matr3 + matr2
    
#     return size_matr2() + matr
        
# print(size_matr())


# Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.


# 8

# list_ = [1, 2, 3, 4]
# result = sum(map(lambda x: x ** 2, list_))
# print(result)



