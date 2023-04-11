# task 1

# def foo():
#     var = 'переменная foo' 
#     print('переменная в foo: ', var) 

#     def bar(): 
#         global var 
#         var = 'переменная bar' 
    
#     bar()
# foo() 

# print('переменная в foo: ', var)

# task 2

# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print(x)
#     x = 'Я могу изменяться'
#     return x

# my_func()
# print(x)
    
# task 3

# num = 3
# def mul():
#     global num
#     num = num ** 2

# mul()
# mul()
# mul()
# print(num)    

# task 4

# balance = 0

# def get_salary(amount):
#     global balance
#     balance += amount

# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

# task 5

# result = 0

# def pow_first(x,y):
#     global result
#     result = x ** y
#     return result

# def pow_second(z):
#     global result
#     result = result % z
#     return result

# pow_first(2, 3)
# pow_second(3)
# print(result)

# task 6

# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age_control():
#     global a
#     for k in a.keys():
#         if a[k] >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')

# age_control()

# task 7

# a = ['father', 'mother', 'brother', 'sister'] 
# b = [] 
# for i in a: 
#     b.append(i.capitalize()) 
# print(b)

# task 8

# def count_symbols(str_):
#     glasnye = []
#     soglasnye = []
#     other = []
#     for letter in str_:
#         if letter.lower() in 'уеёыаоэяию':
#             glasnye.append(letter)
#         elif letter.lower() in 'йцкнгшщзхъфвпрлджчсмтьбю':
#             soglasnye.append(letter)
#         else:
#             other.append(letter)
#     return f'Количество гласных: {len(glasnye)}, согласных: {len(soglasnye)}, остальных символов:  {len(other)}'

# print(count_symbols('Привет как дела'))


# def count_symbols(str_):
#     glasnye = 0
#     soglasnye = 0
#     other = 0
#     for letter in str_:
#         if letter.lower() in 'уеёыаоэяию':
#             glasnye += 1
#         elif letter.lower() in 'йцкнгшщзхъфвпрлджчсмтьбю':
#             soglasnye += 1
#         else:
#             other +=1
#     return f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов:  {other}'

# print(count_symbols('Привет как дела'))

# task 9

# a = []
# a = [x for x in range(11)]
# print(a)

# task 10

# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3, 10, 5]

# def lower_7():
#     global a
#     list_nums = []
#     list_nums = [x for x in a if x < 7]
#     return list_nums

# print(lower_7())

        







