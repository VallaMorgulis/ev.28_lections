# task 1

# try:
#     pass
# except:
#     pass 
# else:
#     pass 
# finally:
#     pass

# task 2

# try: 
#     b = 10
#     c = 11
#     print(a)
# except NameError: 
#     print('Такой переменной не существует!') 

# task 3

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')

# task 4

# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 + num2)
# except ValueError:
#     print('Введите число!')

# task 5

# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_['key3'])
# except KeyError:
#     print('Нет такого ключа!')

# task 6

# list_ = [1, 4, 9, 16, 25, 36] 
# try:
#   print(list_[5])
# except:
#   print('Нет такого элемента!')


# task 7

# try: 
#   age = int(input()) 
#   if age < 18: 
#     raise ValueError('Доступ запрещён') 
# except: 
#   print('Введён некорректный возраст') 
# else: 
#   print('Спасибо') 
# finally: 
#   print('До свидания!')


# task 8

# try:
#   num1 = int(input())
#   num2 = int(input())
#   print(num1 / num2)
# except (ValueError, ZeroDivisionError):
#   print('Произошла ошибка!')
        

# task 9


# try: 
#   cash = int(input()) 
#   if cash < 0: 
#     raise Exception ('ValueError') 
#   print(cash) 
# except: 
#   print('Сумма не может быть отрицательной!')

# task 10

# try:
#   list_ = [1, 2, 3]
#   list_.get(1)
#   print(list_)
# except AttributeError:
#   print('Нет такого метода у списков')

# task 11

# try:
#   string = 'fdrte'
#   num = 3
#   print(string + num)
# except TypeError:
#   print('Unsupported option')


# task 12

# try:
#   for i in range(0, 10):
#       list_.append(i)
#   print(list_)
# except NameError:
#    print('Не объявлена переменная List')



# task 13

# try:
#   list_ = [1, 2, 3, 4]
#   for i in range(0, len(list_) + 1):
#       print(list_[i])
# except IndexError:
#    print('Вы оказались вне индекса')

# task 14

# try: 
#   password = 'short' 
#   if len(password) < 6: 
#     raise ValueError() 
# except ValueError: 
#    raise ValueError 

# task 15

# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
#     [1,4],
#     [2,76],
#     [65,65],
#     [8,6],
#     [0,32],
#     [7,0,3,5]
# ]

# for x in warehouse:
#   if len(warehouse) > 10 or len(x) > 3:
#     raise ValueError(print('Error'))
    
# task 16

# def to_fahrenheit(k:int) -> float:
#     assert k >= 0, 'Холоднее абсолютного нуля!'
#     c = (k - 273.15) * 9/5 + 32
#     return c
    
# print(to_fahrenheit(5))    


# task 17

# try:
#   import lamabimgo
# except ModuleNotFoundError:
#   print('Такого модуля нет')

# task 18

'''Код написанный мной'''

# def clean_spec_symbols(text: str) -> str:
#     speсial_symbols = '!@#$%.,?*()/\|\'":'
#     for s_symbol in speсial_symbols:
#         if s_symbol in text:
#             text = text.replace(s_symbol, '')
#         return text

# def filter_comment(comment: str, banlist=[]) -> None:
#     comment = clean_spec_symbols(comment).lower().split()
    
#     for word in comment:
#         if  word in banlist:
#             raise ValueError ('Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст')

'''Код присланный'''

# def filter_comment(comment: str, banlist=[]) -> None:
#     words = comment.lower().split()
#     for word in words:
#         word = word.strip(",.!?")
#         if word in banlist:
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")

# task 19

# try:
#     num = 100_000_000
#     for i in range(0, num):
#         print("Nope")
# except KeyboardInterrupt:
#     print("Nope")

# task 20

# ['+', '-', '*', '/', '%', '**']

def collect_all_possibles(list_: list, num: int) -> list:
    
















