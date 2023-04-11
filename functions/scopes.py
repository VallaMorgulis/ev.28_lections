# Область видимости и простраства имен ( scopes)
# это технология, которая определяет контекст имени (переменные), в рамках которой мы можем ее использовать.

# built-ins(Встроенная область видимости) -> print, len, max
# global(Глобальная область вилимости -> область одного файла)
# enclosed(не локальна(замкнутая)), nonlocal)
# local(локалная) -> область внутри одной функции


# x = 200

# def myFunc():
#     print(x)
#     a = 300
#     print(a)
#     return a

# myFunc()
# # print(a)
# print(x)

# a = 10 # global
# print # buil-in
# def hello(): # global
#     a = 'Hello world' # local
#     print(a, 'local inside in func')

# hello()
# print(a, 'global')

# LEGB - local enclosed global built-in

# ------------------------------------

# Enclosed 
# замкнутое просторанство имен - локальное пространство, у которого есть внутреннее (вложенное пространство) локальное пространство

# x = 'global'
# print(x, '1')

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3') # local
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

# a = 5

# def func():
#     print(a) # 5
#      a = a + 1

# func()

# global -> позволяет изменять значение глобальной переменной находясь внутри локальной области
# nonlocal -> позволяет изменять значение не локальной(замкнутой) переменной находясь внутри локальной области

# var = 100
# def increment():
#     global var
#     var += 1 # var = var + 1

# print(var)
# increment()
# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)


# СЧЕТЧИК ИДЕАЛЬНЫЙ

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# c = counter() 
# # print(c)    #  <function counter.<locals>.increment at 0x7faaa0a26050>
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# print(c()) # 5

# def func():
#     return 'John Snow'

# a = func

# print(a())


# print(dir(__builtins__))
# print(len(dir(__builtins__)))



# print(globals())

# globals - function которая возвращает все имена внутри глобальной области видимости

# locals - function которая возвращает все имена внутри глобальной области видимости и локальной



# # ИГРА!!!

# def counter():
#     num = 0
#     def increment():
#         nonlocal num
#         num += 1
#         return num
#     return increment

# def showStats(heroes, mobs):
#     print()
#     print(f'John Snow ты убил: \n\tгероев: {heroes} \n\tмобов: {mobs}')
    
    
# counter_heroes = counter()
# counter_mobs = counter()
# heroes = 0
# mobs = 0
# print('Приветствую, король севера John Snow, в вестеросе')

# while True:
#     print('Тебе доступны следующие действия: ')
#     print('1-убить героя, 2-убить моба, 3-статистка, 4-выйти из игры')
#     choice = input('Введите, что хотите сделать: ').strip()
#     if choice == '1':
#         print()
#         heroes = counter_heroes()
#         print('Вы обезглавили Ланистера!')
#     elif choice == '2':
#         mobs = counter_mobs()
#         print()
#         print('Вы убили Белого ходака!')
#     elif choice == '3':
#         showStats(heroes, mobs)
#     elif choice == '4':
#         print()
#         print('Пока пока! Ждем еще раз!')
#         break
    










