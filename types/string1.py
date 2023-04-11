# 'strig - строки'
# "Hello world $&@*&@*$*$&HJHF SJFI090243////z||||\\\\\\fdsjfjewir;wi"

# """
# Hello world

# """
# '''
# Hello world
# '''
# Строки - набор последовательных символов, которые мы используем для хранения и представдения текстовой информации

#  Индексация в строке
# name = 'John'
#         # J = 0 = -4
#         # o = 1 = -3
#         # h = 2 = -2
#         # n = 3 = -1
# print(name)
# print(name[1])
# str1 = 'kani'
# print(str1[-1], str1[0])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[0], str1[1], str1[2], str1[3], str1[4])

# str1 = 'birthday'
# print(str1[5] + str1[6] + str1[7])
# print(str1[0] + str1[1] + str1[2] + str1[3] + str1[4])

# Срезы по индексам
# [start: end: <step>]

# str1 = 'birthday'
# print(str1[5:])
# print(str1[:5])

# text = 'Hello world. My name is John! I\'m King of North!'
# print(text[:13])
# print(text[:])
# print(text[::-1])

# Конкатенация строк (соединение)
# a = 'Hello'
# b = 'World'
# c = a + ' ' + b
# print(c)

# Экранирование - это способ записи символов в строку, которые невозможно ввести с клавиатуры
#-> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикадбная табудяция
# \f -> перевод страницы
# \r -> возврат указателя
#print('\vHello \tworld. \nMy name is John! \nI\'m King of North!')

# Форматирование строк
# 1. с помощью %
# 2. с использование .format
# 3. Интерполяция строк (преобразование, f-stroki)

# %
# name = input('Vvedite imy: ')
# last_name = input('Vvedite familia: ')
# #print('Добро пожаловать к нам' + ' ' + name + ' ' + last_name + '!')
# print('Добро пожаловать к нам %s %s!' %(name, last_name) )

# .format
# name = input('Vvedite imy: ')
# last_name = input('Vvedite familia: ')
# klub = 'Makers'
# print('Приветствую вас, {} {} в нашем клубе {}!' .format(name, last_name, klub))

# f-stroki
# a = input('Enter mr/mrs: ')
# name = input('Vvedite imy: ')
# last_name = input('Vvedite familia: ')
# print(f'Hello {a} {name} {last_name}! Welcome to the party!')


# text = 'Запомни Питтер, с большой силой приходит и большая ответственность.'
# reversed_text = text[::-1]
# # print(reversed_text)
# i = 0
# count_t = 0
# # print(len(reversed_text))
# len_text = len(reversed_text)
# while i < len_text:
#     symbol = reversed_text[i]
#     if symbol == 'т' or symbol == 'Т':
#         count_t += 1
#     #print(symbol)
#     i += 1

# print(f'В тексте "т" встретилась {count_t} раз!')

