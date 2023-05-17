 # task 1

# def call_function(func):
#     def wrapper():
#         print(f'Вызываю функцию {func.__name__}')
#         func()
#         print(f'Вызов функции {func.__name__} прошёл успешно')
#     return wrapper

# @call_function
# def first():
#     print("hello world")
#     return "hello world"

# first()

# task 2

# from datetime import datetime

# def func_start_time(func):
#     def wrapper():
#         print(f'Функция запущена {datetime.now()}')
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()

# task 3

# def make_bold(func):
#     def wrapper():
#         res = '<b>' + func() + '</b>'
#         return res
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         res = '<i>' + func() + '</i>'
#         return res
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         res = '<u>' + func() + '</u>'
#         return res
#     return wrapper   

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())

# task 4

# import time 
# def benchmark(func): 
#     def wrapper():
#         start = time.time()
#         func() 
#         print(f'Время выполнения: {time.time() - start} секунд.') 
#     return wrapper 

# @benchmark
# def fetch_webpage(): 
#   import requests 
#   webpage = requests.get('https://google.com') 

# fetch_webpage()

# task 5

# users = {'John': '3284ui', 'Jammy': '20983iikeke'}

# def validate_password(func):
#     def wrapper(user_, pass_):
#         if not user_ in users.keys():
#             print('Username is not defined')
#         elif users[user_] != pass_:
#             print('Password is invalid')
#         else:
#             return func(user_, pass_)
#     return wrapper

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')



# users = {'jaanger': '123312', 'vlad': '46456', 'nazar': '456132', 'tima': '456123'}
# login('jaanger', '123312')

# task 6

# def is_admin(func):
#     def wrapper(dict_):
#         if dict_['is_admin'] == True:
#             user = dict_['username']
#             print(f'Доступ разрешен {user}')
#             func(dict_)
#         else:
#             user = dict_['username']
#             print(f'Доступ запрещен {user}')
#             return
#     return wrapper

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})

# task 7

# def route(func):
#     def wrapper(path):
#         path = 'https://www.mywebsite.com/' + path
#         return func(path)
#     return wrapper
     
# @route
# def get_page(path):
#      return path
 
# print(get_page('about/'))
# print(get_page('products/'))

# task 8

# def sort_names(func):
#     def wrapper(person):
#         person.sort(key=lambda x: x[2])
#         return func(person)
#     return wrapper
 
# @sort_names
# def prefix_name(person):
#     list_ = []
#     for x in person:
#         if x[3] == 'M':
#             list_.append(f'Mr. {x[0] + " " + x[1]}')
#         else:
#             list_.append(f'Ms. {x[0] + " " + x[1]}')  
#     return list_              
 
# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))

# task 9

# def get_full_number(func):
#     def wrapper(list_):
#         res = [f'+996 {num_[1:4] + " " + num_[4::]}' for num_ in list_]
#         func(res)
#     return wrapper

# @get_full_number
# def sort_phone_nums(list_):
#     list_.sort()
#     str_ = '#'.join(list_)
#     print(str_)
 
# sort_phone_nums(['0777987456', '0555123456', '0770369852'])

# task 10

# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper2(func_arg):
#             if correct_type == type(func_arg):
#                 func(func_arg)
#             else:
#                 print('Неверный тип данных :(')
#         return wrapper2
#     return wrapper
 
# @type_check(int)
# def func1(num):
#     print(num*2)
 
# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})