# str
# ''
# 'Hello'
# str(5)

# print(dir(str))
# print(dir(int))

# a = 'Hello'
# b = 'John'
# print(a != b)
# print('abc' == 'abc')
# print(a > b)
# print(a < b)

# print('a') # 97
# print('h' > 'c') #104 > 99
# Сравнивает так ASCII коды, но не строки

#len() - возвращает количество символов в строке
# a = 'Hello'
# b = 'John Snow'
# print(len(a) < len(b))
# print(len(a), len(b))

# >, <, ==, !=, >=, <=

# Методы строк
# replace(old, new, [count]) - меняет в строке символы old на new, если вы укажите count, то заменит count раз

# text = 'ha ha ha ha'
# result = text.replace('a', 'e', 2)
# print(text)
# print(f'pesult after replace {result}')

# str1 = 'Hello World! My name is John Snow'
# result = str1.replace('John Snow', 'Jammy Lanister')
# print(result)

# strip() - убирает пробельные символы и в конце
# rstrip, lstrip
# a = '   Hello   '
# print(len(a))
# print(a)
# res = a.strip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit    -   проверяют состоит ли наша строка полностью из чисел
# isnumeric
# isdecimal

# num = input('Vvedite chislo: ')
# print(f'Vvedeno chislo?: {num.isdigit()}')

# num = input('Vvedite chislo: ')
# if num.isdigit():
#     num = int(num)
#     print(f'{num} + 5 = {num + 5}')
# else:
#     print('Vy vvely ne chisla!')

# text = '\u0031'
# print(text)
# print(text.isdecimal())
# print(text.isnumeric())
# print(text.isdigit())

# isalnum() - проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы.

# str1 = '56aекаппдэ'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())

# isalpha() - Состоит ли строка полностью из букв

# text = 'Hello World'
# res = text.replace(' ', '')
# print(res)
# # print(res.isalpha())

# islower()
# isupper()
# istitle()
# str1 = 'Is.:'
# print(str1.islower())
# print(str1.istitle())
# str2 = 'IS.:'
# print(str2.isupper())



# index(value, [start], [end]) - выводит индекс значения value, которое мы передаем, в нашей строке.

# text = 'Hello john snow'
# print(text.index('john', 2, 5))


# text = 'Hello world! My name is John Snow!'
# #print(text.index('John'))
# res = text.index('o')
# print(res) # 4
# res = text.index('o', res + 1)
# print(res) # 7
# res = text.index('o', res + 1)
# print(res) # 25
# res = text.index('o', res + 1)
# print(res) # 31


# count(value, [start]) - считает количество вхождений value в нашу строку

# text = 'hello o o o hello'
# res = text.count(' ')
# print(res)

# split(separator) - дробит нашу строку на несколько частей по разделителю, все части строк сохраняются в типе list

# text = 'Makers Bootcamp Only One In The World'
# res = text.split(' ')
# print(res)
# print(len(res))

# a = '#hello#hello#hello#hello'
# res = a[1:].split('#')
# print(res)

# 'connector'.join(list) -> соединяет по connector строки, которые находились в list

# text = 'Makers Bootcamp Only One In The World!'
# res = text.split(' ')
# print(res)
# str1 = ' '.join(res)
# print(str1)

# find(value, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1

# text = 'hello'
# print(text.find('l'))
# print(text.index('fgg'), type(text.find('fgg')))

# swapcase() - Переводит символы нижнего регистра в верхний, а верхнего – в нижний
# upper() - Преобразование строки к верхнему регистру
# lower() - Преобразование строки к нижнему регистру 

# text = 'Hello WoRld, JOHN snow'
# print(f'Original: {text}')
# print(text.upper())
# print(text.lower())
# print(text.swapcase())

# capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
# title() - Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний

# name = input('Vvedite imia: ').capitalize()
# print(name)
# print(f'Hello! Mr/Mrs {name}!')

# fio = 'joHn edvArd snow'
# print(fio.title())

# print(dir(str))



