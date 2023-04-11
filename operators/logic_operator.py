# Операторы сравнения
# Условные операторы и логические сравнения

# Операторы сравнения
# <, >, ==(равно), != (не равно), <=, >=

# 1 < 5 -> True
# 7 > 9 -> False

# Python3 в терминале запускает проверку кода любого без принта. Выйти exit()

# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает если в condition if придет true
# [elif] <condition>:
#     <body elif>
# [else]:
#     <body else> # сработает если во всех вышестоязих условиях пришло False

# string = input('Enter smt: ')

# if string.lower() == 'hello':
#     print('Hello, It\'s me\n was wondering if after all these years wou\'d like to meet')
# elif string.lower() == 'john':
#     print('welcome back John Snow! The King of North!')
# elif string.lower() == 'fkdfkjfairjf kljdflk;sd':
#     print ('Sim Salomon')
# else:
#     print('Совпадений не найдено')

# print('Registration Form:')
# email = input('Enter your email: ')
# password = input('Enter the password: ')
# if len(password) < 8:
#     raise ValueError('Password is too short!\nNeed to be 8 symbols or more!')
# elif password.isdigit():
#     raise ValueError('Password is invalid! Password must contain symbols too!')
# elif password.isalpha():
#     raise ValueError('Password is invalid! Password must contain number or special symbols too!')

# password2 = input('Enter password confirmation: ')

# if password != password2:
#     raise ValueError('Passwords did not match!')

# print(f'Succesfully registred! Hello Mr/Mrs {email}')




# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid value for age!')


# if age < 18:
#     print(f'Access Denied! Come again after {18 - age} year(s)')
# else:
#     print('You can pass! Welcome to KZ!')


# and - логическое И
# or - логическое ИЛИ
# not - огическое ОТРИЦАНИЕ

# money = 1_000_001
# status = 'premium'

# if money > 1_000_000 and status == 'premium':
#     print('You are president of our club!')
# elif money > 1_000_000 or status == 'premium':
#     print('You are ministr of our club!')
# else:
#     print('You are honorable member of our club!')

# str1 = 'Hello World'
# print(str1)
# symbol = input('Enter the symbol: ')

# if symbol not in str1:
#     print(f'The symbol: {symbol} does not exist!')
# else:
#     print(f'The symbol: {symbol} exist!')

# str1 = 'Hello World'
# print(str1)
# symbol = input('Enter the symbol: ')

# if symbol in str1:
#     print(f'The symbol: {symbol}' exist!')
# else:
#     print(f'The symbol: {symbol} does not exist!')


# разрешаем доступ если он юзер гита или гугла и его возврат больше 21 или у него деньги (10000)
# user = 'John'
# is_google_user = True
# is_github_user = False
# age = 22
# user_coins = 9000

# if (is_google_user or is_github_user) and (age > 21 or user_coins > 10000):
#     print(f'You can enter the system Mr/Mrs {user}!')
# else:
#     print('Sorry, you couldn\'t enter!')


