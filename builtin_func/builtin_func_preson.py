# my_list =  ['m', 'a', 'k', 'e', 'r', 's'] 
# import functools 
# new_word = functools.reduce(lambda x, y: x + y, my_list) 
# print(new_word) 

# task 1

# list_ = [1, 2, 3, 4]  
# import functools 
# new_word = functools.reduce(lambda x, y: x + y, list_) 
# print(new_word) 

# task 2
'''
from functools import reduce
items = [1, 24, 17, 14, 9, 32, 2, 100, -60]
all_max = reduce(lambda a, b: a if (a > b) else b, items)
 
print (all_max)
'''

# list_ = [5, 8, 4, 6, 7] 
# result = all(x > 3 for x in list_) 
# print(result)

# task 3
'''
list1 = ['some', 'string', '42']
new_list1 = any(str.isdigit() for str in list1) 
print(new_list1)
'''

# list_ = [5, 8, 4, 6, 7, 4]
# result = any(x < 0 for x in list_) 
# print(result)


# task 4

'''nums = [1, 2, 3, 4, 5, 6, 7] 
new_nums = list(map(lambda x: x ** 3, nums)) 
print(new_nums) '''

# list_ = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, list_))
# print(result)

# task 5

'''fruits = ['apple', 'banana', 'grapes', 'apricot'] 
result = list(filter(lambda x: x.startswith('a'), fruits))
print(result)'''

# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)

# task 6

# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)

# task 7

# list_ = [5, 6, 7, 8] 
# from functools import reduce
# result = reduce(lambda x, y: x * y, list_ )
# print(result)

# task 8

# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0, list_)))
# result = f'even: {list2}, odd: {list3}'
# print(result)

# task 9





# list_ = [
#     'hello',
#     6, 
#     [1,2,3]
# ]

# num = 2

# def collect_all_possibles(list_: list, num: int) -> list:
#     list_new = []
#     for i in list_:
#         try:
#             if type(i) == str:
#                 list_new.append(i * num)
#             elif type(i) == int:
#                 list_new.append(i + num)
#                 list_new.append(i - num)
#                 list_new.append(i * num)
#                 list_new.append(i ** num)
#                 list_new.append(i // num)
#             elif type(i) == list and list:
#                 list_new.append(i * num)
#         except ZeroDivisionError:
#            print('Ошибка! Деление на 0!')
#         finally:
#             return list_new
    
# print(collect_all_possibles(list_, num))


# list_ = [
#     'hello',
#     6, 
#     [1,2,3]
# ]

# num = 2

# def collect_all_possibles(list_: list, num: int) -> list:
#     res = []
#     for i in list_:
#         try:
#             res.append(i + num)
#         except:
#             pass
#         try:
#             res.append(i - num)
#         except:
#             pass
#         try:
#             res.append(i * num)
#         except:
#             pass
#         try:
#             res.append(i ** num)
#         except:
#             pass
#         try:
#             res.append(i // num)
#         except:
#             pass
#     return res

# a = collect_all_possibles(list_, num)
# print(a)



# my_dict = {}


# # словарь с ключами — целочисленными значениями
# my_dict = {1: 'яблоко', 2: 'мяч'}


# # словарь с ключами разных типов
# my_dict = {'имя': 'Джон', 1: [2, 4, 3]}


# # используем dict()
# my_dict = dict({1:'яблоко', 2:'мяч'})


# # словарь из последовательности, где элементы являются парами
# my_dict = dict([(1,'яблоко'), (2,'мяч')])
# my_dict[3] = 'груша'
# del my_dict[2]
# print(my_dict)