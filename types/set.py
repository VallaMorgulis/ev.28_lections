# Set() - множества.
# Это изменяемый неупорядоченный, итерируемый, но не индексируемый тип данных.

# множества хранят в себе только не изменяемые типы данных

# a = ['febw']
# print(hash(a))

# 1. -> set()
# a = set([1,2,3,4,5])
# print(a)

# a = set({1:2, 3:4})
# print(a)

# 2. - {,}
# set2 = {1, 2, 3}
# print(a)

# set1 = {1, 0, True, False}
# print(set1)

# frozenset неизменяемое множество
# a = frozenset([1,2,3,4,5])
# a.add(7)
# print(a)

# Методы! SET

# add -> для добавления

# set1 = {1,2,3}
# set1.add(4)
# print(set1)
# set1.add((1,2,3,4,5))
# print(set1)
# set1.add((1,2,3,4,5))
# print(set1)

# update - он может добавлять несколько значений сразу, но не провторяя имеющийся и он добавляет все итеррируемые.

# set1.update({3: '1', 4: '5'})
# print(set1)
# set1.update('string', {1,2,3,4,5,6,7})
# print(set1)

# set1.update([1,2,3,45,6, 'string'])
# print(set1)

# УДАЛЕНИЕ В SET

# 4 метода
# clear - очищает все множества
# remove(element) - принимает элемент определенные и если этого элемента нет выдает ошибку
# discard(element) - не возвращает ошибку
# pop() - удаляет из set(FIFO) first In first Out - первое вхождение

# set1 = {1,2,3,4,5}
# set1.remove(9)
# set1.clear()
# set1.discard(5)
# a = set1.pop()
# b = set1.pop()
# print(set1)
# print(a, b)
# print(set1.pop())

# difference - выводит отличие первого множества от второго
# set2 = {1,2,3,4}
# set1 = {2,3,5,7,8}
# print(set1.difference(set2))

# print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)
# print(set1)

# print(set1.intersection(set2)) # - выводит не уникальные значения
# print(set1 & set2) # - тоже самое

# print(set1.union(set2)) # объединяет
# print(set1 | set2) # - тоже самое

# --------------------------------

# a = [1,2,3,4]
# b = [2,3,5,7,8]

# set1 = set(a)
# set2 = set(b)

# print(set1.difference(set2))

# -------------------------------

# a = list(input())
# print(len(a) == len(set(a)))

# tuple - реизменяемый, индексируемый, итерируемый, упорядоченный тип данных

# index(element) - возвращает индекс этого элемента в кортеже
# литералы ()
# a = (True, 'a', 1, 2, 1, 1)
# print(a, type(a))
# b = tuple()
# print(a.index(1))
# print(b, type(b))
# c = ()
# print(c, type(c))

# count(element) - возвращает число вхождений элементов в кортеж
# print(a.count('a'))

# tuple = (1,2,3,4,5,6,7,8)
# target = 5
# # index of target
# print(tuple.index(target))

# set1 = {1,2,3,4,5}
# set1.remove(9)
# set1.clear()
# set1.discard(5)
# set1.update('lol')
# print(set1.pop())
# print(set1)







