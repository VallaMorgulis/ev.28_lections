# Обработка исключений
# операторы try..except

#Errors -> связаны с кодом
    # SyntaxError
    # IndentationError
    # TabError

# Исключения exceptions -> связаны с неправильными данными которые передаются в код

    # ZeroDivisionError
    # ArithmeticError
    # NameError
    # IndexError
    # KeyError
    # BaseException # прородитель всех исключений

# try:
#     a = int(input('Enter the number: '))
# except:
#     print('неправильные данные')
# else:
#     print(a * 5)

# try:
#     <body>
# except:
#     <body> сработает если есть ошибка
# else:
#     <body> сработает если нет ошибки
# finally:
#     <body> сработает в любом случае
# ls = ['John', 'Snow', 'Tirion']

# try:
#     i = int(input('Vvedite Index: '))
#     print(ls[i])
# except (ValueError, IndexError):
#     print('что то пошло не так')

# ls = ['John', 'Snow', 'Tirion']
# print(ls)
# try:
#     i = int(input('Vvedite Index: '))
#     print(ls[i])
# except ValueError:
#     print('вы ввели не правильные данные')
# except IndexError:
#     print('вы ввели не правильные индекс')

# --------------------------------------------------
# отображение ошибки
# Exception as e (error)
# dict_ = {'1': 'one', '2': 'two', 'name': 'John'}

# try:
#     key = int(input('Vvedite key: '))
#     print(dict_[key])
# except Exception as e:
#     print(f'Opps {e.__class__} error!')

# try:
#     num1 = int(input('Inter num1: '))
#     num2 = int(input('Inter num2: '))
#     result = num1 / num2
# except ValueError:
#     print('Invalid input')
# except ZeroDivisionError:
#     print('Na 0 delit\' nel\'za!')
# else:
#     print(result)
# finally:
#     print('The End!')


    


