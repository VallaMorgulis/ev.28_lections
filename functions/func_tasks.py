# task 1

# def add(num1, num2):
#     return num1 + num2

# task 2

# def get_string_length(len_str):
#     return len(len_str)

# task 3

# def get_type(type1, type2):
#     print(type(type1))
#     print(type(type2))
    
# task 4

# def divide(num1, num2):
#     return (num1 / num2)

# task 5

# dict_ = {1: 'ert', 2: 'cde', 3: 'oiu'}
# def dictionary(dict_):
#     for k in dict_.keys():
#         print(k)
    
# dictionary(dict_)

# task 6

# num = 6
# def check(num):
#     if num % 2 == 0: 
#         return "It is even number" 
#     else: 
#         return "It is odd number"
    
# print(check(num))

# task 7

# def is_palindrome(str_):
#     if str_.lower() == str_.lower()[::-1]:
#         return True
#     else:
#         return False
    
# print(is_palindrome('Mom mor'))

# task 8

# def max_num(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# task 9

# def multiply_list(num_list: list) -> int:
#     multiply = 1    
#     for i in num_list:
#         multiply = multiply * i
        
#     return multiply

# print(multiply_list([1, 2, 3, 4, 5, 6]))

# task 10

# def sum_digits(num):
#     str_num = str(num)
#     summa = 0
#     for i in str_num:
#         if i.isdigit():
#             summa += int(i)

#     return summa

# print(sum_digits(105))

# task 11

# def func11(x, y, z):
#     if z != 0:
#         res = (x + y) / z
#         return res
#     else:
#         res = (x + y)
#         return res

# task 12

# def func12(list_, up_or_low):
#     end_list = []
#     for item_ in list_:
#         if up_or_low == 'lower':
#             end_list.append(item_.lower())
#             return end_list
#         elif up_or_low == 'upper':
#             end_list.append(item_.upper())
#             return end_list

# task 13

# def func13(str_):
#     dict_ = {k: str_.count(k) for k in str_ }
#     return dict_

# task 14

# def add_(num1: int, num2: int) -> int: return num1 + num2

# def sub_(num1: int | float, num2: int | float) -> int |  float:
#     return num1 - num2

# def mult_(num1: int | float, num2: int | float) -> int |  float:
#     return num1 * num2

# def div_(num1: int | float, num2: int | float) -> int |  float:
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'

# def calc(num1, num2, operation):
#     if operation == '+': return add_(num1, num2)
#     elif operation == '-': return sub_(num1, num2) 
#     elif operation == '*': return mult_(num1, num2)
#     elif operation == '/': return div_(num1, num2)   
#     else: return 'Вы ввели неверный оператор'

# task 15

# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]

# def func15(users):
#     send = []
#     for user in users:
#         if user['work'].startswith('IT'):
#             send.append(f"{user['name']}, скидки в магазине компьютерной техники!\n")
#     send_messages = ''.join(i for i in send)
#     return send_messages

# print(func15(users))

# task 16

# def func16(km, l_gas):
#     spend_gas = l_gas / km * 100
#     return (f'На 100км было расходовано {round(spend_gas)}л горючего')

# print(func16(600, 35))

# task 17

# employees = [
#     {'name': 'Pack', 'salary': 10000, 'overTime': 4}, 
#     {'name': 'Rom', 'salary': 15000, 'overTime': 3}, 
#     {'name': 'Gessica', 'salary': 20000, 'overTime': 9}, 
#     {'name': 'Kelen', 'salary': 25000, 'overTime': 2}, 
#     {'name': 'Weter', 'salary': 30000, 'overTime': 0}
#     ] 


# def func17(add_salary):
#     for person in add_salary:
#         if 'overTime' != 0:
#             person['salary'] += person['overTime'] * 200
#             person.pop('overTime')
#         else:
#             person.pop('overTime')

#     return add_salary

# print(func17(employees))

# task 18

# list_ = ['John', 1, 34, '544', 'Snow', 'Sansa', 234, '43',' Stark']

# def func18(list_):

#     list_num = []
#     list_str = []
#     for i in list_:
#         if type(i) == str:
#             list_str.append(i)
#         else:
#             list_num.append(i)

#     return (list_num, list_str)

# task 19

# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(list_):
#     list_.sort(key=lambda x:x['marks'],reverse=True) 
#     return list_

# print(func19(students))

# task 20

# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]

# def func20(list_, str_):
#   list_sorted = []
#   for goods in list_:
#       if str_.lower() in goods['title'].lower():
#           list_sorted.append(goods)

#   return list_sorted

# print(func20(products, 'I'))
        

# task 21

# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ] 

# def func21(list_, str_):
#   list_cat = []
#   for i in list_:
#     if str_.lower() == i['category']:
#       list_cat.append(i)
#   return list_cat

# print(func21(products, 'xiaomi'))

# task 22

# balance=9_999_999 

# def spent(a,b,c): 
#     if c-b>=0: 
#         c-=b 
#         return ({'target':a,'spend':b},c) 
#     else: 
#         return 'Недостаточно средств' 
    
    
# print(spent('neger',20000,balance)) 

# def deposit(a,b): 
#     b+=a 
#     return b

# task 23

# database = list()

# def create(database, title, price, category):
#     database.append({'title': title, 'price': price, 'category': category})
#     return database

# def read(database):
#     print(database)
#     return database

# def update(database, index, title, price, category):
#     database[index]['title'] = title
#     database[index]['price'] = price
#     database[index]['category'] = category
#     return database

# def delete(database, index):
#     database.pop(index)
#     return database






















