# Инкапсуляция:
# 1. Языковая конструкци которая помогает связать данные с методами для их обработки и управления (это связь между данными и методами, которые управляют ими) (класс - это и есть капсула)
# 2. Механизм сокрытия при помощи которого можно ограничить доступ оного компонента программы к другому.

# Инкапсуляция как связь

# class Phone:
#     number = '+99700700700'

#     def print_number(self):
#         print(f'Мой номер: {Phone.number}')
#         print(f'Мой номер: {self.number}')


# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия
#3 уровня сокрытия данных в питоне
    # 1. Публичный (public) - number, print_number
    # 2. Защищенные (_protected) - _number
    # 3. Приватный (private) - __number

# class Car:
#     _country = "Germany"

#     def __init__(self) -> None:
#         self.marka = 'Mersedes Benz' # public
#         self._model = 'w140'  # protected
#         self.__color = 'grey' # private

# obj = Car()
# print(dir(obj))
# print(obj._Car__color)
# print(obj._country)
# print(obj._model)

# class Phone:
#     username = 'John'
#     _caller = 'Jamie'
#     __count_of_calls = 15

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('взять трубку(y/n): ')
#         if question.lower().strip() == 'y':
#             self.__turn_on()
#         else:
#             print('бросили трубку!')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

#     def __turn_on(self):
#         self.__increment_calls()
#         print('Allo!')
#         print(f'Count of calls with {self._caller}: {self.__count_of_calls}')

# john = Phone()
# print(john.username)
# john.call()
# john.call()
# john.call()
# john.call()

#--------------------------------------

# class Person:
    
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def display_info(self):
#         print(f'My name is {self.name} and I am {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()
# obj.nationality = 'Kyrgyz'
# print(obj.nationality)
# obj.age = -18
# obj.name = 55
# obj.display_info()

#---------------------------
# getter and setter
# они нудны чтобы избежать прямого обращения к сокрытым атрибутам при этом можно добавить логику валидацию(проверка) данных которые будет установлены в атрибут


# class Person:
#     def __init__(self, name, age) -> None:
#         self.__name = name
#         self.__age = age
    
#     def display_info(self):
#         print(f'My name is {self.__name} and I am {self.__age} years old!')

#     def name(self):
#         return self.__name

#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Name must be str obj!')
#         else:
#             self.__name = name

#     def age(self):
#         return self.__age

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age < 150:
#             print('Invalid value for age!')
#         else:
#             self.__age = age

# obj = Person('John', 24)
# print(obj.name())
# obj.set_age(-18)
# obj.display_info()
# obj.set_name("Raichle")
# obj.display_info()


3
