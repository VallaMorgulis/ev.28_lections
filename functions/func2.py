# str1 = 'Hello world! My name is John, last name is Snow. Nice to meet you!'
#     # VAR 1
# # def reverse(string):    
# #     b = string.split()
# #     c = b[::-1]
# #     d = ' '.join(c)
# #     return d

# # print(reverse(str1))

#     # VAR 1
# def get_reverser_string(text):
#     spisok = text.split()[::-1]
#     return ' '.join(spisok)

# print(get_reverser_string(str1))
# print(get_reverser_string('Hello John иди в жопу плиз - задолбал'))


# def sum_of_args(a, b, c=5, d=5): # параметры
#     return a + b + c + d

# result = sum_of_args(1, 2, 3, 4) # аргументы
# print(result)
# res = sum_of_args
# # print(res, type(res))
# print(res(5,6,7,8))
# print(sum_of_args(5, 5))

# ----------------------------------

# позицилннные и именнованиые аргументы
# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(5, 10 ,15)
# print()
# printParams(c=5, b=15, a=10)
# print()
# printParams(c=20, b=30, a=15)


# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments (позиционные)
# print(sum_of_args(a=5, c=20, b=10, d=15)) # keywords arguments (имееные)
# print(sum_of_args(5, 20, c=10, d=15))

# -----------------------------------

# оператор *
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, *b]
# print(c)

# ----------------------------------

# *args, **kwards в функциях

# def printScores(studet, *args):
#     print(f'Name of studet: {studet}')
#     # print(args)
#     print(f'AVG: {sum(args) / len(args)}')
#     for x in args:
#         print('Score:', x)

# printScores('John Snow', 100, 90, 80, 95, 88)

# def printPetNames(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     for pet, name in pets.items():
#         if type(name) == list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# printPetNames('John Snow', dog='Pluto', cat='Garfid', fish=['Nemo', 'Doru', 'Batya'], turtle='Leonardo')

# def get_some_date(a, b, *args, **kwargs):
#     print('параметры а и b:', a, b)
#     print('аргументы:', [*args]) # если просто args то будет tuple
#     print('именованные аргументы:', kwargs)

# get_some_date(1,2,3,4,5, lang='Python', car='BMW')

# ГЕНЕРАТОР ПАРОЛЕЙ

# def generate_random_string(len_):
#     import string as s
#     import random
#     # print(s.ascii_letters, s.digits, s.punctuation)
#     symbols = s.ascii_letters + s.digits
#     res = [
#         random.choice(symbols) for i in range(1, len_)
#      ] + list(random.choice(s.punctuation))
#     random.shuffle(res)
    
#     return ''.join(res)

# print(generate_random_string(15))

#-----------------------------------------------

# def is_palindrome(string):
      
#     if string.lower().strip() != string[::-1].lower().strip():
#         return False
#     else:
#         return True
    
# print(is_palindrome('mart ere ere tram'))


