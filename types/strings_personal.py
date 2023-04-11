# find(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
# rfind(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
# index(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
# rindex(str, [start],[end]) - Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
# replace(шаблон, замена) - Замена шаблона
# split(символ) - Разбиение строки по разделителю
# upper() - Преобразование строки к верхнему регистру
# lower() - Преобразование строки к нижнему регистру 
# swapcase() - Переводит символы нижнего регистра в верхний, а верхнего – в нижний
# startswith(str) - Начинается ли строка с шаблона str
# title() - Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
# capitalize() - Переводит первый символ строки в верхний регистр, а все остальные в нижний
# endswith(str) - Заканчивается ли строка S шаблоном str
# isdigit() - Состоит ли строка из цифр
# isalpha() - Состоит ли строка из букв
# isalnum() - Состоит ли строка из цифр или букв
# islower() - Состоит ли строка из символов в нижнем регистре
# isupper() - Состоит ли строка из символов в верхнем регистре
# isspace() - Состоит ли строка из неотображаемых символов (пробелов, табуляции)
# istitle() - Начинаются ли слова в строке с заглавной буквы
# strip() - Она используется для возврата копии исходной строки путем удаления начальных и конечных пробелов, символов, переданных в функцию strip()

# stroka = 'Makers Bootcamp'
# print(stroka.find('Bootcamp'))

# stroka = 'Makers Bootcamp'
# print(stroka.rfind('oot'))

# stroka = 'Makers Bootcamp'
# print(stroka.index('t'))

# stroka = 'Makers Bootcamp'
# print(stroka.rindex('oot'))

# stroka = 'Makers Bootcamp'
# res = stroka.replace('Makers Bootcamp', 'Makakers Bezshtans')
# print(res)

# stroka = 'Makers #Bootcamp #Only #One #In #The #World'
# res = stroka.split()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.lower()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.swapcase()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.startswith('Bootcamp')
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.title()
# print(res)

# stroka = 'MAKERS BOOTCAMP ONLY ONE IN THE WORLD'
# res = stroka.capitalize()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.endswith('Makers')
# print(res)

# stroka = '43842780374'
# res = stroka.isdigit()
# print(res)

# stroka = 'MakersBootcampOnlyOneInTheWorld'
# res = stroka.isalpha()
# print(res)

# stroka = 'Makers2Bootcamp3Only4One5In6The7World'
# res = stroka.isalnum()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# res1 = res.islower()
# print(res1)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.upper()
# res1 = res.isupper()
# print(res1)

# stroka = '              ' # пробелы и табуляция
# res = stroka.isspace()
# print(res)

# stroka = 'Makers Bootcamp Only One In The World'
# res = stroka.istitle()
# print(res)

# ВОТ РАБОТА МЕТОДОВ СТРОК И СПИСКОВ ДЛЯ ПЕРЕВОДА ИЗ СТРОКИ В СПИСОК И ОБРАТНО ПЛЮС РАЗДЕЛЕНИЕ СТРОК ПО ЭЛЕМЕНТУ

# hashtags = '#makers#bootcamp#программирование#it#курсы'
# print(hashtags)
# hashtags1 = hashtags.replace('#', ' ')
# hashtags2 = hashtags1.lstrip(' ')
# hashtags3 = hashtags2.split(' ')
# print(hashtags3)

# hashtags4 = '#' + '#'.join(hashtags3)
# print(hashtags4)


# Task15
# string = 'abracadabra'
# print(string[0:5] + 'K' + string[6:])

# Task16
# string = 'hELLO wORLD'
# print(string.swapcase())

# Task17
# string = 'hELLO wORLD\n'
# print(string * 3)

# Task18
# string = ' Makers'
# ind = string.find('e') 
# print(ind)

#Task19
# string = 'python is the best'
# print(string.startswith('Python')) 

# Task20
# string = '123456789a'
# print(string.isdigit())

# Task21
# string = 'Hello World'
# print(string.split(' '))

# Task22
# string = input()
# print(f'Hello {string}')

# Task23
# string1 = 'Hello'
# string2 = 'World'
# print(f'{string1} {string2}')

# Task24
# string1 = "America" 
# string2 = "Japan" 
# print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])

# Task25
# string = "    Как прекрасен этот мир!   " 
# res = string.strip() 
# print(f'{res}\n{len(res)}')

# Task 26
# string = "cow loves good milk" 
# print(string.replace("o", "e", 2))





