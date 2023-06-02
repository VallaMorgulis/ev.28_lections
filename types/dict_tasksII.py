# task 1

# a = {'x': 1, 'y': 2, 'z': 1}
# print(list(a)[0])

# task 2

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.pop('b')
# print(b)

# task 3

# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

# task 4

# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

# task 5

# a = {'a': 1, 'b': 2, 'c': 1}
# b = list(a.keys())
# print(b)

# task 6

# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# task 7

# a = {'a': 1, 'b': 2, 'c': 1}
# for k in a:
#     print(k)

# task 8

# a = {'a': 1, 'b': 2, 'c': 1}
# for v in a.values():
#     print(v)

# task 9

# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {k: 2 if v % 2 == 0 else v for k, v in a.items()}
# print(b)

# task 10

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {k: v for k, v in a.items() if v}
# print(b)

# task 11

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# b = {k: v / 5 for k, v in a.items()}
# print(b)

# task 12

# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)
# print(a)

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# a = {k:v for k,v in a.items() if v % 2 != 0}
# print(a)

# task 13

# a = {'a': 1, 'b': 2, 'c': 3} 
# b = {v:k for k, v in a.items()}
# print(b)

# task 14

# a = {'a': 3, 'b': 2}
# b = sum({v for v in a.values()})
# print(b)

# a = {'a': 3, 'b': 2}
# b = sum(a.values())
# print(b)

# task 15

# a1 = dict(a=1, b=2)
# a2 = {x:x*2 for x in range(1, 20)}
# a3 = dict(zip(a1, a2))
# print(a1)
# print(a2)
# print(a3)

# task 16

# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('y'))

# task 17

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)

# task 18

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())

# task 19

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(max(dict_.values()))

# task 20

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# print(min(dict_.values()))

# task 21

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6}
# dict2 = {k:1 if v % 2 != 0 else v for k,v in dict1.items()}
# print(dict2)

# task 22

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# dict_ = {k:v for k,v in dict_.items() if not v}
# print(dict_)

# task 23

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {k**2:v for k,v in dict1.items()}
# print(dict2)

# task 24

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {x:len(x) for x in list_}
# print(dict_)

# task 25

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5}
# dict_max = max(dict_.values())
# for k in dict_.keys(): 
#     if dict_[k] == dict_max: 
#         print(k)

# task 26

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {k:v**3 for k,v in dict1.items()}
# print(dict2)

# task 27

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# dict_ = {k:inner_v for k,v in dict_.items() for inner_v in v.values()}
# print(dict_)

# task 28
# import math
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {k:math.prod(v.values()) for k,v in dict1.items()}
# print(dict2)

# dict3 = {}
# for k,v in dict1.items():
#     res = 1
#     for y in v.values():
#         res = res * y
#     dict3[k] = res

# print(dict3)

# task 29

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# str_ = [x for x in list_ if isinstance(x, str)]
# int_ = [x for x in list_ if isinstance(x, int)]
# dict_ = dict(zip(str_, int_))
# print(dict_)

# task 30

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k:item for item in sorted(dict_.values()) for k,v in dict_.items() if item == v}
# print(sorted_dict)

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=lambda x: x[1]))
# print(sorted_dict)

# task 31

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {k:item for item in sorted(dict_.values(), reverse=True) for k,v in dict_.items() if item == v}
# print(sorted_dict)

# def myFunc(e): 
#     return e[1] 
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=myFunc, reverse=True))
# print(sorted_dict)

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=lambda x: x[1], reverse=True))
# print(sorted_dict)

# task 32

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# if key in dict_:
#     print('Key is present in the dictionary')
# else:
#     print('Key is not present in the dictionary')

# task 33

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {**dict1, **dict2, **dict3}
# print(dict4)

# task 34

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = dict(zip(list1, list2))
# print(dict_)

# task 35

# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# summa = dict_['math']['sum'](dict_['vars'].values())
# print(summa)

# task 36

# a = {'a': 10, 'b': 9, 'c': 3}
# import math
# result = math.prod(a.values())
# print(result)

# task 36

# string = "pythonist" 
# dict_ = {x:string.count(x) for x in string}
# print(dict_)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = dict(sorted(list(dict_.items()), key=lambda x: x[1]))
# print(sorted_dict)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {k: x for k,v in my_dict.items() for x in v.values()} 
# print(dict_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [x if x >= 0 else 1 for x in list_]
# print(int_list)

# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [x for x in list1 if isinstance(x, str)]
# print(list2)

# list_ = [0, 3, 9, 7, 5, 2, 18, 4]
# list1 = [x for x in list_ if x > 5]
# print(list1)


      