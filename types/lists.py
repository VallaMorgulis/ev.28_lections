# list() -> (списки, массив) - изменяемый, последовательный тип данных, который представляет из себя коллекцию каких либо объектов (значения).

# my_list = [1, 'string', False, None, [1,2,3,4,5]]
# print(my_list, type(my_list))

# range() - возвращает последовательность элементов (чисел)
# ls = range(1, 101)
# my_list = list(ls)
# print(my_list)

# list()

# my_list = list('Hello world')
# print(my_list)

# tuple_ = ('banana','apple','cherry')
# print(tuple_, type(tuple_))
# ls = list(tuple_)
# print(ls, type(ls))

# Индексация в списках
# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls, len(ls))
# print(ls[1], ls[2])
# print(ls[4:])

# ls = [1, 2, 3, 4, 5, 'string', [True, False, None]]
# print(ls[6][:-1])

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# ls = list(range(1, 11))
# print(ls)
# for num in ls:
#     print(num)

# ls = ['John', 'Sansa', 'Tirion', 'Eddart','Serseya', 'Jamie']
# print(ls, len(ls))
# for x in ls:
#     if x == 'Serseya':
#         print(f'Hello {x}! Welcome to New York!')
#         print(x)

# # print('2')
# ls = list(range(1, 21))
# for x in ls:
#     if x % 2 == 0:
#         print(f'Число четное {x}, квадрат: {x**2}')
#     else:
#         print(f'Число нечетное {x}, куб: {x**3}')

# -------------------------------------------------------------------------

# Методы списков
# print(dir([]))
# append(element) - Добавление элементов в конец списка

# ls = [1, 2, 3]
# print(ls)
# ls.append(4)
# ls.append(5)
# ls.append('Hello')
# ls.append([True, False])
# print(ls)

# extend(object) - расширяет список
# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# ls.extend(str(56))
# ls.extend([1, 2, 3])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# sort() - сортирует список, если передать reverse=True, то список отсортируетя в убывающем порядке

# from random import randint
# ls = []
# for x in range(0, 100):
#     num = randint(0, 1000)
#     ls.append(num)

# print(ls)
# ls.sort(reverse=True)
# print("After:")
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Aizirek', 'azalya']
# ls.sort(key=len, reverse=True)
# print(ls)

# insert(index, element) - добавляет элемент по указанному index

# ls = ['string', 2, 3, False]
# ls.insert(1, [1, 65, 3, 'ertyy', True])
# print(ls)

# remove(element) - удаляет элемент из списка и если такого нет, выводится ошибка
# pop([index]) - удаляет и возвращает элемент из списка по index, но если index не передать, то удаляет последний элемент

# ls = [5, 1, 2, 4, 4, 5, 5, 5]
# # ls.remove(5)
# # print(ls)
# # print(5 in ls)

# while 5 in ls:
#     ls.remove(5)

# print(ls)

# ls = [5, 1, 2, 4, 5, 5]
# # print(ls.pop(5)) # 5
# # print(ls.remove(5))  # None
# deleted = ls.pop()
# print(ls)
# print(deleted)

# update-----------------------------------------
# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)
# ls.reverse()
# print(ls)
# print(ls[::-1])

# pizza = ['first_item', 'second_item', 'third_item', 'forth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)


# ВОТ КАК СПИСОК СДЕЛАТЬ ИЗ СТРОКИ И ОБРАТНО

# numbers = 'Hello gdgdsgd dfdf' 

# numbers2 = list(numbers.split())

# print(f'{numbers}\n{numbers2}')

# hello = ' '.join(map(str, numbers2))
# print(hello)




