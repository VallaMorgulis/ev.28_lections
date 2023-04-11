flag = True
simbols = '0123456789' + '-' + '.' # 0123456789-.

while flag:
    print()
    num1 = input('Введите первое число: ')
    is_correct_number = True
    for x in num1:
        if x not in simbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break

    if not is_correct_number:
            continue
    

    num2 = input('Введите второе число: ')
    for x in num2:
        if x not in simbols:
            print('Вы ввели неправильное число!')
            is_correct_number = False
            break

    if not is_correct_number:
            continue
    
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('Введите оператор(+, -, *, /, //, %, **): ').strip()

    if operator == '+':
        print(f'Результ: {num1 + num2}')
    elif operator == '-':
        print(f'Результ: {num1 - num2}')
    elif operator == '*':
        print(f'Результ: {num1 * num2}')
    elif operator == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'Результ: {num1 / num2}')
    elif operator == '%':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'Результ: {num1 % num2}')
    elif operator == '//':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'Результ: {num1 // num2}')
    elif operator == '**':
        print(f'Результ: {num1 ** num2}')
    else:
        print('Вы ввели не верный оператор!')

    choice = input('Хотите продолжить (y/n)? ')
    if choice.lower().strip() != 'y':
        flag = False
        print('Пока пока')