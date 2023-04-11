# task 11
# string = 'hello'
# print (string[-1] + string[1:-1] + string[0])

# task 12
# hashtags = '#makers#bootcamp#программирование#it#курсы'
# hashtags1 = hashtags.lstrip('#')
# print(hashtags1.split('#'))

# hashtags = '#makers#bootcamp#программирование#it#курсы'
# hashtags1 = hashtags.lstrip('#').split('#') 
# print(hashtags1)

# ВОТ КАК МОЖНО ВЫЗЫВАТЬ МЕТОДЫ!!! НО ЕСЛИ ПЕРЕДАН ПАРАМЕТР, ПОСЛЕ НЕГО БЕЗ ПАРАМЕТРОВ НИКАК :)
# hashtags = '#makers#bootcamp#программирование#it#курсы'
# res = hashtags.upper().lstrip('#').split('#')
# print(res)


# Task 13
# name = input('Vashe imya: ')
# last_name = input('Vasha familiu: ')
# age = input('Vash vozvrast: ')
# city = input('Vash gorod: ')
# print(f'Вас зовут {name} {last_name}, Ваш возраст: {age}, Вы проживаете в городе {city}')

# task 14
# string = 'Makers bootcamp'
# print(string[1::2])

# task 15
# string = 'abracadabra' 
# print(string[0:5] + 'K' + string[6:])

# task 16
# string = 'hELLO wORLD'
# print(string.swapcase())

# task 17
# string = 'hello world'
# print((string + '\n') * 2 + string)

# task 18
# string = '...Makers'
# print(string.find('e'))

# task 19
# string = 'Python is the best'
# print(string.startswith('Python'))

# task 20
# string = '123456789'
# print(string.isdigit())

# task 21
# string = ' Hello World'
# print(string.split())

# task 22
# string = input()
# print(f'Hello {string}')

# task 23
# string1 = 'Hello'
# string2 = 'Makers'
# print(f'{string1} {string2}')

# task 24
# string1 = "America"
# string2 = "Japan"
# print(string1[0] + string2[0] + string1[int(len(string1[0:])/2)] + string2[int(len(string2[0:])/2)] + string1[-1] + string2[-1])

# string1 = "America" 
# string2 = "Japan" 
# print(string1[:1] + string2[:1] + string1[int(len(string1)/2)] + string2[int(len(string2)/2)] + string1[-1] + string2[-1])

# task 25
# string = '          Как прекрасен этот мир!   '
# text = string.strip()
# count = str(len(text))
# print(text + '\n' + count)

# string = " Как прекрасен этот мир! " 
# res = string.strip() 
# print(f'{res}\n{len(res)}')

# task 26
# string = "cow loves good milk"
# print(string.replace('o', 'e', 2))



# string = "          Как прекрасен этот мир!   "
# print(f'{string.strip()}\n{len(string.strip())}')