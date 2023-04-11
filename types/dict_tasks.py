# task 1
# a = {'x': 1, 'y': 2, 'z': 1}
# ls = a.keys()
# ls = list(ls)
# print(ls[1])

# a = {'x': 1, 'y': 2, 'z': 1} 
# print(list(a.keys())[0])

# task 2
# a = {'a': 1, 'b': 2, 'c': 1}
# removed = a.pop('a')
# print(removed)

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
# list_ = list(a.keys())
# print(list_)

# task 6
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

# task 7
# a = {'a': 1, 'b': 2, 'c': 1}
# for key in a:
#     print(key)

# task 8
# a = {'a': 1, 'b': 2, 'c': 1}
# for k, v in a.items():
#     print(v)

# task 9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {}
# for k, v in list(a.items()):
#     if v % 2 != 0:
#         b.setdefault(k, v)
#     else:
#         b.setdefault(k, 2)

# print(b)

# task 10

# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

# for k, v in list(a.items()):
#     if v == None:
#         a.pop(k)

# print(a)

# task 11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 

# for k, v in list(a.items()):
#     a.update({k: v/5})

# print(a)

# task 12

# a = {'apple': 2, 'orange': 5, 'banana': 10}
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a.pop(k)

# print(a)

# task 13

# a = {'a': 1, 'b': 2, 'c': 3} 
# b = {}
# for k, v in a.items():
#     b.setdefault(v, k)

# print(b)

# task 14

# a = {'a': 3, 'b': 2} 
# print(sum(a.values()))

# task 15
# ls = list(range(1, 100))
# a1 = dict.fromkeys(ls, 'value')
# print(a1)

# a2 = {"a": 1,"b": 2,"v": 3}
# print(a2)

# a3 = {}
# a3.update({'age': 25, 'address': 'BlackCastle'})
# print(a3)

# task 16

# dict_ = {'x': 1, 'y': 2, 'z': 1}
# a = dict_.get('z')
# print(a)

# task 17

# удаляем методом DEL

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['a']
# print(dict_)

# удаляем генератором нового словаря

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# dict_ = {key:dict_[key] for key in dict_ if key != 'a'}
# print(dict_)

# task 18

# dict_ = {'a': 1, 'b': 2, 'c': 1}
# items = dict_.items()
# print(items)

# task 19

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

# a = 0
# for k, v in dict_.items():
#     if v > a:
#         a = 0
#         a = a + v

# print(a)

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21} 
# b = {} 
# for k,v in dict_.items(): 
#     if True: 
#         b.setdefault(v) 
        
# print (max(b))

# task 20

# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}

# b = {} 
# for k,v in dict_.items(): 
#     if True: 
#         b.setdefault(v) 
        
# print (min(b))

# task 21

# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 

# dict2 = {}
# for k,v in dict1.items():
#     if v % 2 != 0:
#         dict2.setdefault(k, 1)
#     else:
#         dict2.setdefault(k, v)

# print(dict2)

# task 22

# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k,v in list(dict_.items()):
#     if v != None:
#         dict_.pop(k)

# print(dict_)

# task 23

# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k,v in dict1.items():
#     dict2.setdefault(pow(k,2),v)

# print(dict2)

# task 24

# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}

# for i in list_:
#     dict_.setdefault(i, len(i))

# print(dict_)

# task 25

# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5} 
# max_ = max(dict_.values()) 

# for k in dict_.keys(): 
#     if dict_[k] == max_: 
#         print(k) 
    
# task 26

# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}

# for k,v in dict1.items():
#     dict2.setdefault(k, pow(v, 3))

# print(dict2)

# task 27

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# for k,v in list(dict_.items()): 
#     for v2 in v.values(): 
#         dict_[k] = v2 
        
# print(dict_)

# task 28

# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k,v in dict1.items():
#     a = 1
#     for v2 in v.values():
#         a = a * v2 
#     dict2.setdefault(k, a)

# print(dict2)

# task 29

# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# key = []
# value = []

# for i in list_:
#     if type(i) == str:
#         key.append(i)
#     elif type(i) == int:
#         value.append(i)
# dict_ =  dict(zip(key, value))
# print(dict_)

# task 30

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_values = sorted(dict_.values()) 
# sorted_dict = {} 
# for i in sorted_values: 
#     for k in dict_.keys(): 
#          if dict_[k] == i: 
#             sorted_dict[k] = dict_[k] 
#             break 

# print(sorted_dict)

# task 31

# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_values = sorted(dict_.values(), reverse=True) 
# sorted_dict = {}
# for i in sorted_values: 
#     for k in dict_.keys(): 
#          if dict_[k] == i: 
#             sorted_dict[k] = dict_[k] 
#             break 

# print(sorted_dict)

# task 32

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} 
# key = input() 
# if key in dict_: 
#     print("Key is present in the dictionary") 
# else: 
#     print("Key is not present in the dictionary")

# Это мое рабочее зешение ниже, но более грамоздкое -------

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input())
# a = 0
# for k in dict_.keys():
#     if k == key:
#         a = a + 1

# if a == 1:
#     print('Key is present in the dictionary')
# else:
#     print('Key is not present in the dictionary')

# task 33

# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# dict4 = {**dict1, **dict2, **dict3}
# print(dict4)

# task 34

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# i = 0
# for k in list1:
#     dict_[k] = list2[i]
#     i += 1

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

# res = dict_.get('vars')
# summa = dict_['math']['sum'](res.values())
# print(summa)

# task 36

# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for k in a:
#     result = result * a[k]

# print(result)

# task 37

# string = "pythonist"
# dict_ = {}
# for i in string:
#     dict_[i] = string.count(i)

   
# print(dict_)




