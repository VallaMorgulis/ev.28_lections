# task 1

# list_ =  [x for x in range(1, 101)]
# print(list_)

# task 2

# list_ = [n for n in range(1, 50) if n % 2 != 0]
# print(list_)

# task 3

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [n for n in list_ if n % 2 == 0 and n > 0]
# print(int_list)

# task 4

# list_ = [x ** 2 for x in range(1, 26)]
# print(list_)

# task 5

# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(x) for x in str_list]
# print(int_list)

# task 6

# list_ = [x if x % 2 != 0 else x * x for x in range(1, 11)]
# print(list_)

# task 7

# list_ = [False if x % 2 != 0 else True for x in range(1, 11)]
# print(list_)

# task 8

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name]
# print(new_list)

# task 9

# dict_ = {num: num ** 2 for num in range(1, 11)}
# print(dict_)

# task 10


# n = int(input())
# dict_ = {i: i ** 2 for i in range(1, 501) if i % n == 0}
# print(dict_)

# try:
#    n = int(input('Vvedite chislo')) 
# except ValueError:
#    print('Invalid number')
# else:
#    dict_ = {x: x ** 2 for x in range(1, 501) if x % n == 0}

# task 11
''' ЭТО РЕШЕНИЕ ВЕРНОЕ НО ТОЛЬКО ЗДЕСЬ
a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {}

for k, v in a.items():
    list_ = [i for i in range(1, v+1)]
    dict_[k] = list_

print(dict_)
'''
''' ЭТО ВЕРНОЕ ДЛЯ ТАСКОВ НО НАПИСАНО НЕ МНОЙ - БЕЛАЛ НАПИСАЛ
a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k: [i for i in range(1, v + 1)] for k, v in a.items()}
print(dict_)
'''

'''А это уже мое решение спустя полторы месяца'''
'''a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k:[x for x in range(1, v+1)] for k,v in a.items()}
print(dict_)'''

# task 12

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'even' if v % 2 == 0 else 'odd' for k, v in dict_.items()}
# print(a)

# task 13

# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [x for x in string_.split() if x.isdigit()]
# print(list_)

# task 14

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
#  'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# new_dict = {k: k2 for k, v in dict_.items() for k2, v2 in v.items() if max(v.values()) == v2}
# print(new_dict)

# task 15

# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

# dict_ = {k: v2 for k, v in my_dict.items() for k2, v2 in v.items()}
# print(dict_)

# task 16

# list_ = [x for x in range(1, 26) if x % 2 == 0]
# print(list_)

# task 17

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x if x >= 0 else 1 for x in list_]
# print(int_list)

# task 18

# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [x for x in list1 if type(x) == str]
# print(list2)

# task 19

# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x > 5]
# print(list1)

# task 20

# list_ = [False, True, False, True, False, True, False, True, False, True] 
# new_list = [1 if x == True else 0 for x in list_]
# print(new_list)

# task 21

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = [len(x) for x in list_name]
# print(new_list)

# task 22

# a = [x for x in range(1, 1001, 125) if x % 2 == 0]
# print(a)

# task 23

# list1 = [44,54,64,74,104]
# list2 = [x + 6 for x in list1]
# print(list2)

# task 24

# list1 = [2, 4, 6, 8, 10, 12, 14]
# new_list = [x for x in list1 if x ** 2 > 50]
# print(new_list)

# task 25

# string = "happy birthday!"
# list_ = [x for x in string if x != ' ' and x != '!']
# print(list_)

# task 26

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# inner_list = [v2 for x in dict_.values() for v2 in x.values()]
# print(inner_list)

# task 27

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# dict_ = {v: len(v) ** 2 for v in list_name if len(v) > 4}
# print(dict_)

# task 28

# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list_ = [key.upper() for key, value in dict_.items() if value >= 200 and value <= 5000]
# print(list_)

# task 29

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {k.replace('i', ''): k.count('i') for k, v in dict1.items()}
# print(dict2)

# task 30

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [x for x in list1 if x != None and x != [] and x != {} and x != '' and x != 0]
# print(list2)

# task 31

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]
# readers = [reader[0] for reader in SPL_Patrons if reader[1] > 100]
# print(readers)

# task 32

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# saved_amount  = [round(books[1] * 11.95, 2) for books in SPL_Patrons]
# print(saved_amount)

# task 33

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# pirate_price_corns = [[x[0], x[1] * 42] for x in prairie_pirates if x[2] == True]
# print(pirate_price_corns)

# task 34

# dict_ = { 'Sasha': { 'likes': 23, 'comments': 2, 'rating': 4 }, 'Aliya': { 'likes': 34, 'comments': 5, 'rating': 5 }, 'Dasha': { 'likes': 15, 'comments': 3, 'rating': 2 }, 'Luna': { 'likes': 12, 'comments': 2, 'rating': 1 }, 'Rena': { 'likes': 26, 'comments': 7, 'rating': 2 } } 
# sum_likes = [v['likes'] for v in dict_.values() if v['rating'] > 3]
# print(sum(sum_likes))

# task 35

# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# dict1 = [b['id'] for value in dict_.values() for b in value['comments'] if len(value['comments']) > 3]
# print(dict1)

# task 36

# list_ = [x / 2 for x in range(0, 11) if x % 2 == 0]
# print(list_)

# task 37

# dict_ = {1: 'first', 2: 'second', 3: 'third', 4: 'fourh', 5: 'fifth'}
# dict_ = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()}
# print(dict_)


# task 38

# from random import randint

# set1 = {randint(1, 150) for i in range(1, 11)}
# set2 = {randint(1, 150) for i in range(1, 11)}
# full_set = set1 | set2
# if len(full_set) < 20:
#     print(f'В этом сете было {20 - len(full_set)} повторения, его длина составляет {len(full_set)}')
# else:
#     print('Ваш объединенный сет полностью уникальный!')


dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
new_list = [item for v in dict_.values() for item in v.values()]
print(new_list)













