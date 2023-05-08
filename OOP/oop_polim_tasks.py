# task 1

# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# list_ = (a, b, c)
# for item in list_:
#     print(len(item))

# task 2

# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex) 

# task 3

# class Person:
#     def __init__(self, name, last_name) -> None:
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'

# class Employee(Person):
#     def __init__(self, name, last_name, work, status) -> None:
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#     def __init__(self, name, last_name, university, course) -> None:
#         super().__init__(name, last_name)
#         self. university = university
#         self.course = course

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self. university} на {self.course} курсе'

# person = Person('Иван', 'Петров')
# employee = Employee('Рога и Копыта', 'директор','Иван', 'Петров')
# student = Student('КГТУ', '3','Иван', 'Петров')

# def get_human_info(obj):
#     print(obj.get_info())

# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)

# task 4

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):

#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height

#     def get_area(self): 
#         return self.base * self.height * 0.5

# class Square(Shape):
#     def __init__(self, length) -> None:
#         self.length = length

#     def get_area(self):
#         return self.length ** 2      

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2


# triangle = Triangle(8, 12)
# square = Square(6)
# circle = Circle(7)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 

# task 5

# class OS:
#     def __init__(self, version) -> None:
#         self.version = version

# class Windows(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами COMMAND + C'
    
# class Linux(OS):
#     def copy(self, text):
#         self.text = text
#         return f'скопирован текст "{self.text}" горячими клавишами CTRL + SHIFT + C'
    
# win = Windows(3)
# mac = MacOS(4)
# lin = Linux(5)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# task 6

# class Language:
#     def __init__(self, level, type) -> None:
#         self.level = level
#         self.type = type

# class Python(Language):
#     def write_function(self, func_name, arg): 
#         return f"def {func_name}({arg}):" 

#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"{var_name} = '{value}'" 
#         else: 
#             return f"{var_name} = {value}" 

# class JavaScript(Language): 
#     def write_function(self, func_name, arg): 
#         return f"function {func_name}({arg}) {{ }};" 
    
#     def create_variable(self, var_name, value): 
#         if isinstance(value, str): 
#             return f"let {var_name} = '{value}';" 
#         else: 
#             return f"let {var_name} = {value};" 
        
        
# py = Python('Intermediate', 'Backend') 
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John')) 
# js = JavaScript('Advanced', 'Frontend') 
# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))

# task 7

# class Money:
#     def __init__(self, country, symbol) -> None:
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80

#     def __init__(self, country, symbol) -> None:
#         super().__init__(country, symbol)

#     def exchange(self, amount):
#         return f'$ {amount} равен {amount * self.rate} сомам'

# class Euro(Money):
#     rate = 98.40

#     def __init__(self, country, symbol) -> None:
#         super().__init__(country, symbol)

#     def exchange(self, amount):
#         return f'€ {amount} равен {amount * self.rate} сомам'

# task 8

# class Planet:
#     def __init__(self, orbit): 
#         self.orbit = orbit

# class Mercury(Planet):

#     def __init__(self, orbit):
#         super().__init__(orbit)

#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет' 
  
# class Venus(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)

#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round((earth_age / (self.orbit / 365))*365)} дней'

# class Jupiter(Planet):
#     def __init__(self, orbit):
#         super().__init__(orbit)

#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'
    
# mercury = Mercury(88) 
# venus = Venus(225) 
# jupiter = Jupiter(12) 
# print(venus.get_age(20)) 
# print(jupiter.get_age(20)) 
# print(mercury.get_age(20))


### 1

# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian() 
# obj.ride() 
# obj.swim() 


### 2

# class ContactList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         self.name = name
#         list_same = [x for x in self.list_ if self.name in x]
#         return list_same


# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 


### 3

# class Person:
#     def __init__(self, name=None, last_name=None, age=None, email=None) -> None:
#         self.__name = name
#         self.__last_name = last_name
#         self.__age = age
#         self.__email = email

#     def get_name(self):
#         return self.__name
#     def set_name(self, name):
#         self.__name = name

#     def get_last_name(self):
#         return self.__last_name
#     def set_last_name(self, last_name):
#         self.__last_name = last_name

#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         self.__age = age

#     def get_email(self):
#         return self.__email
#     def set_email(self, email):
#         self.__email = email

# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com











        

