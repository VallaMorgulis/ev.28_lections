# task 1

# a = {1, 1, 2, 'd', 5, '232', 'ddf', 'er', '%'}
# print(a)

# task 2

# a = {'hello', 'world', 21}
# print(len(a))

# task 3

# a = {'Jane', 'Eyre', 22}
# a.add('Hello world!')
# print(a)

# task 4

# a = {1, 2, 3}
# b = {3, 4}
# a.update(b)
# print(a)

# task 5

# a = {1, 2, 3}
# a.discard(4)
# print(a)

# task 6

# a = {1, 2, 3}
# a.remove(9)
# print(a)

# task 7

# a = {1, False, 3}
# a.clear()
# print(a)

# task 8

# a = {4, 6, 100, -45, -6}
# b = {4, 5, -5, -6}
# print(a.intersection(b))

# task 9

# a = {2, 4, 6, 50, -45, -6} 
# b = {4, 3, 5, -5, -6}
# print(a.difference(b))

# task 10

# 1 способ объединения
# a = {2, 4, 5, -45, -6}
# b = {4, 3, 5, -5, 2}
# print(a.union(b))

# 2 способ объединения
# a = {2, 4, 5, -45, -6}
# b = {4, 3, 5, -5, 2}
# print(a | b)

# task 11

# a = {0, 1, 2}
# b = {0, 1, 2, 3, 34, 5, 8, 13}
# if a.issubset(b):
#     print('Подмножество!')

# task 12

# a = {0, 1, 2, 3, 34, 5, 8, 13} 
# b = {1, 2, 34}
# if a.issuperset(b):
#     print('Надмножество!')

# task 13

# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10}

# if not robert.isdisjoint(kail) and not robert.isdisjoint(merri):
#     print("kail merri")
# elif not robert.isdisjoint(kail):
#     print("kail")
# elif not robert.isdisjoint(merri):
#     print("merri")
# else:
#     print('no one')

# task 14

# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'} 
# timur = {'OchakKebab', 'FreshBox'} 
# alexander = {'FreshBox', 'KFC'} 
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'OchakKebab', 'KFC'}
# print(tilek & timur & alexander & elina)

# task 15

# ingredients = {"cыр чеддар", "грибы", "соус", "шпинат"} 
# ingredients.add("помидор")
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add("базилик")
# ingredients.discard('cыр чеддар')
# ingredients.add("сыр моцарелла")
# print(ingredients)

# task 16

# a = [set(), set(), set()]
# inp1 = input() # Hello world
# inp2 = int(input()) # 1-3
# if inp2 == 1:
#     a[inp2 - 1].update([inp1])
#     a[inp2].update(['default value'])
#     a[inp2 + 1].update(['default value'])
# elif inp2 == 2:
#     a[inp2 - 1].update([inp1])
#     a[inp2 - 2].update(['default value'])
#     a[inp2].update(['default value'])
# elif inp2 == 3:
#     a[inp2 - 1].update([inp1])
#     a[inp2 - 3].update(['default value'])
#     a[inp2 - 2].update(['default value'])
# else:
#     a[0].update(['default value'])
#     a[1].update(['default value'])
#     a[2].update(['default value'])

# print(a)

# task 17

# set1 = {x for x in range(0, 10) if x % 2 == 0}
# set2 = {x for x in range(0, 10) if x % 2 != 0}

# if set1 & set2:
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')










