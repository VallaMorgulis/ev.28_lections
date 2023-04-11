def add(num1: int, num2: int) -> int: return num1 + num2

def subtract(num1: int | float, num2: int | float) -> int |  float:
    return num1 - num2

def multiply(num1: int | float, num2: int | float) -> int |  float:
    return num1 * num2

def divide(num1: int | float, num2: int | float) -> int |  float:
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

def calculate(num1: int | float, num2: int | float):
    '''Наша функция выполняет арифметическую операцию!'''
    operator = input('Введите оператор(+,-,/,*): ')
    if operator == '+': return add(num1, num2)
    elif operator == '-': return subtract(num1, num2) 
    elif operator == '*': return multiply(num1, num2)
    elif operator == '/': return divide(num1, num2)   
    else: return 'Вы ввели неверный оператор'

def main():
    num1 = input('Введите первое число: ')
    num2 = input('Введите второе число: ')
    
    try:
        num1 = float(num1) if '.' in num1 else int(num1)
        num2 = float(num2) if '.' in num2 else int(num2)
    except ValueError:
        print('Вы ввели некорректное число')
        main()
        return

    while True:
        result = calculate(num1, num2)
        if type(result) == str:
            print(f'Результат: {result}')
        else:
            print(f'Результат: {result}')
            break

    question = input('Хотите продолжить?(Y/N): ').lower().strip()

    if question == 'y':
        main()
    else:
        print('Спасибо за использование нашего калькулятора!')

main()


    
    
