#Типы данных числа -> int, float

# = -> оператор присваивания
# variable(переменная)
# num = 5
# print(num) #5
# num = 79 # переопределение
# print(num) #79

# abc -> нижний регистр
# ABC -> верхний регистр

# PEP8
# tomorrow_day = '10.03.2023' #Snake case 
# tomorrowDay = '10.03.2023' #Camel case 

# num1 = 5 
# num2 = 15

# result = num1 + num2
# print('Summa:', result)


# num1 = input('Enter the num1: ') # str
# num2 = input('Enter the num2: ') # str
# num1 = int(num1)
# num2 = int(num2)

# print(num2, '-', num1, "=", num2 - num1)
# *
# num1 = int(input('Enter the num1:'))
# num2 = int(input('Enter the num2:'))
# print(num1, '*', num2, "=", num1 * num2)

# / and // and %
# / - обычное деление
# // - деление без остатка
# % - модульное деление(получение остатка от деления)

# num1 = 7
# num2 = 3

# print('/', num1 / num2) 
# print('//', num1 // num2) 
# print('%', num1 % num2) 

# ** -> возведение в степень
# print(5 ** 2)
# print(16 ** 55)

# print(144 ** 0.5) # квадратный корень числа

# a = 4
# b = 5

# print(id(a))
# print(id(b))

# pow - возведение в степень
# pow(num1, num2, <mod>)
# num1 = 5
# num2 = 10
# print(num1 ** num2)
# print(pow(5, 10))
# print(pow(5, 10, 10))
# print(pow(5 ** 10 % 10))

# a = 5
# b = 2
# res = pow(a, b, 12)
# print(res)

#round() - округление числа с плавающей точкой
# a = 5.328232
# print(round(a, 2))

#abs() - абсолютное значение числа -> abs(-5) -> 5
# a = abs(-16)
# b = abs(15)
# print(a, b)

# divmod(abc, b) -> Она выводит 2 числа, первое число это результат целочисленного деления (//) а на в, а второе число это модульное деление (%)

# res = divmod(5, 2)
# print(res)
# print((5 // 2, 5 % 2))

#print(9 ** 0.5)
# import math
# a = 5
# print(round(math.sqrt(a), 2))

# множественное присваивание
# оператор присваивания (=)
# a = 5
# b = 15
# c = None
# print('a:', a, 'b:', b)

# c = a
# a = b
# b = c
# print('a:', a, 'b:', b)
# a, b = (b, a)
# print('a:', a, 'b:', b)

# num1, num2, num3 = input('Num1: '), input('Num2: '), input('Num3: ')
# print(num1)
# print(num2)
# print(num3)


# from math import pi
# r = int(input('Vvedite: '))
# res_P = 2 * r * pi 
# res_S = pi * r ** 2
# print('S okruzhnosti: ', round(res_S, 2))
# print('P okruzhnosti: ', round(res_P, 2))

# from random import randint

# #print(randint(1, 10))
# name = input('Vvedite svoe imya: ')
# last_name = input('Vvedite svoe familie: ')
# num = randint(1_000_000, 9_999_999)
# #print(name, last_name, num)
# res = name + last_name + str(num)
# print(res)

# from random import randint
# num = randint(1, 10)
# i = 0
# while i < 3:
#     guess = int(input('Ugaday chislo: '))
#     if guess == num:
#         print('You win! Congrads!')
#         break
    
#     #i = i + 1
#     i += 1 # increment

#task 6
# positive = 5
# negative = -5
# print(abs(positive))
# print(abs(negative))

# task 7
# x = int(6)
# print(pow(x, 3))

#task 8
# x = int(7)
# y = int(3)
# print(x % y)

#task 9
# y = int(6)
# print(pow(y, 2, 5))

#task10
# inp1 = int(input())
# inp2 = int(input())
# inp3 = int(input())
# y = (inp1 * inp2)
# print(y % inp3)

#task11
# num1 = int(input())
# num2 = int(input())
# num3 = float(6.6)
# y = (num1 % num2)
# print(y * num3)

#task12
# decimal = float(25)
# print(decimal ** 2)
# print(decimal ** 3)
# print(decimal ** 0.5)

#task13
# leg_a = int(3)
# leg_b = int(4)
# hypotenuse = ((leg_a ** 2) + (leg_b ** 2))
# print(hypotenuse ** 0.5)

#task14
# radius = int(8)
# import math
# s = math.pi * radius ** 2 
# print(s)

# Task21
# temp = float(70)
# print(round((temp - 32) / 1.8, 2))

# Task22
# s = 3738
# print(s *1000)

# day = int(input('Vvedite den svoego rozdenia: ' ))
# month = int(input('Vvedite mesyac svoego rozdenia: ' ))
# year = int(input('Vvedite god svoego rozdenia: ' ))
# print(day + month + year)

# Task 15
# first = 2
# second = 3
# third = 4
# first, third, second = second, first, third
# print(second, first, third)

# task 16
# num = 5
# p = (num + num) * 2
# s = num ** 2
# print(p, s)

#task 17
# length = 5
# hiegth = 13
# p = (length + hiegth) * 2
# s = length * hiegth
# print(p, s)

# task 23
# t = 255
# print(t*1000*1000, t*1000, t*10)

# task 24
# y = 7
# print(y * 12, y * 365)

# task 25
# h = 513 
# f = 2.7 
# fs_ = h / f 
# print(fs_)

#task 26
# d_salary = 2400
# period = 15
# currency = 84
# dollars_total = d_salary * period
# som_total = dollars_total * currency
# print(som_total)

























