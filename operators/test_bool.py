# Task 1

# number = int(input('Vvedite chislo: '))

# if number > 0:
#     print(True)
# else:
#     print(False)

# Task 2
# string = input()
# if int(len(string)) > 5:
#     print(True)
# else:
#     print(False)

# Task 3
# mark = int(input())

# if mark >= 90:
#     print('Отлично, Ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, Ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')

# task 4
# number = int(input('Vvedite chislo: '))

# if number < 0:
#     print('negative')
# elif number > 0:
#     print('positive')
# else:
#     print('zero')

# task 5
# x = 6
# y = 8

# if x < y:
#     print(x)
# else:
#     print(y)

# task 6
# x = 105
# y = 124
# z = 98

# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)

# task 7
# x = 105
# y = 105
# z = 105

# if x == y and y == z and x == z:
#     print(3)
# elif x != y and y != z and x != z:
#     print(0)
# else:
#     print(2)

# task 8
# x = int(input())
# y = int(input())

# if x % y != 0:
#     print(f'x не делится на y\nЧастное: {x // y}\nОстаток: {x % y}')
# else:
#     print(f'x делится на y\nЧастное: {x // y}')

# task 9
# year = int(input())

# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# task 10
# nums = [1, 2, 3, 4, 5]
# target = 5
# if target in nums: 
#      print('Да') 
# else: 
#      print('Нет') 

# task 11
# num = int(input()) # A-Z = 65-90; a-z = 97-122;     

# if (num > 64 and num < 91) or (num > 96 and num < 123):
#     print(f'Это буква "{chr(num)}"') # с помощью chr() получаем из числа Unicode элемента
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')


# num = chr(int(input())) 

# if num.isalpha(): 
#     print(f'Это буква "{num}"') 
# else: 
#     print(f'Это не буква, а символ "{num}"')

# task 12
# greeting = str(input())

# if greeting == 'Hi':
#     print('Привет!')
# else:
#     print('NO')

# task 13
# count = 0
# number = input()
# if number.isdigit():
#     count = int(number)
# print(count)

# task 14
# lang = str('ru') # или 'ru' или 'de' или 'kg'

# if lang == 'en':
#     print('This is english')
# elif lang == 'ru':
#     print('Это русский')
# elif lang == 'de':
#     print('Das ist Deutsch')
# elif lang == 'kg':
#     print('Бул кыргыз тили')

# task 15
# string = str(434434)
# int1 = int(string[0:3])
# int2 = int(string[-3:])

# if int1 == int2:
#     print('да')
# else:
#     print('нет')

# task 16
# a = int(input())
# b = int(input())
# c = int(input())

# if a <= b and a <= c and b <= c:
#     print(a, b, c)
# elif b <= a and b <= c and c <= a:
#     print(b, c, a)
# elif c <= a and c <= b and b <= a:
#     print(c, b, a)
# elif c <= a and c <= b and a <= b:
#     print(c, a, b)
# elif a <= c and a <= b and c <= b:
#     print(a, c, b)
# else:
#     print(b, a, c)

# task 17
# user_age = int(input())

# if user_age < 18:
#     print('Доступ запрещен')
# else:
#     print('Добро пожаловать')

# task 18
# user_num = int(input('Vvedite chislo ot 1 do 12: '))

# if user_num < 1 or user_num > 12:
#     print("Такого месяца нет")
# elif user_num == 1 or user_num == 2 or user_num == 12:
#     print("зима")
# elif user_num == 3 or user_num == 4 or user_num == 5:
#     print("весна")
# elif user_num == 6 or user_num == 7 or user_num == 8:
#     print("лето")
# else:
#     print("осень")

# task 19
# user_str = str(input())

# if user_str.isdigit():
#     print("is digit")
# elif user_str.isalpha():
#     print("is alpha")
# else:
#     print("is ASCII")

# task 20
# lens1 = int(input())
# lens2 = int(input())
# lens3 = int(input())

# if lens1 + lens2 > lens3 and lens1 + lens3 > lens2 and lens2 + lens3 > lens1:
#     print('yes')
# else:
#     print('no')

# task 21
# a1, b1, c1 = int(input()), int(input()), int(input()) 
# c = max(a1, b1, c1) 
# b = min(a1, b1, c1) 
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1) 

# if c >= a + b: 
#     print('impossible') 
# elif pow(c, 2) == pow(a, 2) + pow(b, 2): 
#     print('rectangular') 
# elif pow(c, 2) < pow(a, 2) + pow(b, 2): 
#     print('acute') 
# elif pow(c, 2) > pow(a, 2) + pow(b, 2): 
#     print('obtuse')


# task 22

# n = int(input())
# if n in range(11, 15):
#     print(f'На лугу пасется {n} коров')
# else:
#     temp = n % 10
#     if temp in list(range(5,10))+[0]:
#         print(f'На лугу пасется {n} коров')
#     if temp == 1:
#         print(f'На лугу пасется {n} корова')
#     if temp in range(2,5):
#         print(f'На лугу пасется {n} коровы')


# task 23

# studet_call = int(input())
# if studet_call % 2 == 0:
#     print('второй')
# else:
#     print('первый')

# task 24
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if x1 == x2 or y1 == y2:
#     print('YES')
# else:
#     print('NO')

# task 25
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

# if abs(x2 - x1) == abs(y2 - y1):
#     print('YES')
# else:
#     print('NO')