# sentence = input('Vvedite predlojenie: ')

# if sentence[-1] == '?':
#     print('Yes, voprositel\'noe!')
# else:
#     print('No, normal one!')

# print('Yes, voprositel\'noe!' if sentence[-1] == '?' else 'No, normal one!') 

# Ternary operators(Тернарный оператор) - это конструкция, которая по своему действию аналогична конструкции if/else, но при этом записывется в одну строчку.

# number = int(input('Vvedite chislo'))
# res = 'even number' if number % 2 == 0 else 'odd number'
#         # четное                            #нечетное
# print(res)

# <выражение которое срабатывает если True> if <условие> else <выражение если False>

# ls = [55, 65, 75, 89, 100, 15, 6]
# print(ls)
# choice = input('Vvedite ma[/min: ]')
# res = max(ls) if choice.lower().strip() == 'max' else min(ls)
# print(res)

# if choice.lower().strip() == 'max':
#     print(max(ls))
# elif choice.lower().strip() == 'min':
#     print(min(ls))
# else:
#     print('Invalid choice!')

# res = max(ls) if choice.lower().strip() == 'max' else min(ls) if choice.lower().strip() == 'min' else 'invalid choice'
# print(res)

# КАЛЬКУЛЯТОР

# flag = True
# simbols = '0123456789' + '-' + '.' # 0123456789-.

# while flag:
#     print()
#     num1 = input('Введите первое число: ')
#     is_correct_number = True
#     for x in num1:
#         if x not in simbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break

#     if not is_correct_number:
#             continue
    

#     num2 = input('Введите второе число: ')
#     for x in num2:
#         if x not in simbols:
#             print('Вы ввели неправильное число!')
#             is_correct_number = False
#             break

#     if not is_correct_number:
#             continue
    
#     num1 = float(num1) if '.' in num1 else int(num1)
#     num2 = float(num2) if '.' in num2 else int(num2)
#     operator = input('Введите оператор(+, -, *, /, //, %, **): ').strip()

#     if operator == '+':
#         print(f'Результ: {num1 + num2}')
#     elif operator == '-':
#         print(f'Результ: {num1 - num2}')
#     elif operator == '*':
#         print(f'Результ: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результ: {num1 / num2}')
#     elif operator == '%':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результ: {num1 % num2}')
#     elif operator == '//':
#         if num2 == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(f'Результ: {num1 // num2}')
#     elif operator == '**':
#         print(f'Результ: {num1 ** num2}')
#     else:
#         print('Вы ввели не верный оператор!')

#     choice = input('Хотите продолжить (y/n)? ')
#     if choice.lower().strip() != 'y':
#         flag = False
#         print('Пока пока')

         


   