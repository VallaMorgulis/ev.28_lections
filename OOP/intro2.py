# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, wight, nation) -> None:
#         self.name = f'{first_name} {last_name}'
#         self.wight = wight
#         self.nation = nation

#     def birthday(self):
#         from random import randint
#         print(f'\nHappy birthday, {self.name}!!!')
#         self.age += 1
#         self.wight += randint(3, 7)

#     def show_info(self):
#         print(self.name, self.age, self.wight, self.nation)

# human1 = Human('John', 'Snow', 3.3, 'American')
# human2 = Human('Abu-Bakr', 'Al-Nassr', 3.8, 'Arabic')

# human1.show_info()
# human2.show_info()
# print()
# print('After 1 year:')
# human1.birthday()
# human2.birthday()
# print()
# human1.show_info()
# human2.show_info()
# human1.birthday()
# human2.birthday()
# human1.birthday()
# human2.birthday()
# human1.birthday()
# human1.show_info()
# human2.show_info()

#---------------------------------

# class Student:
#     university = 'Harvard'

#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
#         self.languages = {}
#         self. knowledge = 0
#         self.is_ready_to_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.is_ready_to_work:
#             self.is_ready_to_work = True
#             print(f'{self.name} get 500 points!!!')

#     def read_book(self, book_name):
#         self.books.append(book_name)
#         self.add_points(50)

#     def do_project(self):
#         self.add_points(100)

#     def learn_new_language(self, language, percent):
#         if percent not in range(70, 101):
#             print('Invalid points')
#         else:
#             self.languages[language] = percent
#             self.add_points(percent)
        

# st1 = Student('John Snow')
# st2 = Student('Billal Karimov')  

# print(st1.name)
# print(st2.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Is {st1.name} ready to work: {st1.is_ready_to_work}')

# st1.read_book('Game of Trones')
# st1.read_book('Martin Eden')
# st1.read_book('Algoritms and Data Structures')
# st1.read_book('Eugeniy Onegin')

# st1.do_project()
# st1.do_project()

# st1.learn_new_language('Python', 40)
# st1.learn_new_language('Python', 90)
# st1.learn_new_language('C++', 75)

# print(f'After study {st1.name}: {st1.books}, {st1.languages}, {st1.knowledge}')
# print(f'Is {st1.name} ready to work: {st1.is_ready_to_work}')    

#------------------------------------------------------

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'
    

#     def show_info(self):
#         return f'{self.brand} -> {self.model}'

# obj = Car('BMW', '7 series')
# print(obj)
# # print(obj.show_info())
# obj2 = Car('Lada', 'Sedan')
# print(obj2)
# obj3 = Car('KIA', 'K8')
# print(obj3)

#-----------------------------------

# import random

# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def shoot(self, other):
#         other.health -= 20
#         print(f'Атаковал {self}')
#         print(f'у {other} осталось{other.health}')
    
#     def __str__(self) -> str:
#         return self.name
    
# sniper1 = Sniper('John Snow')
# sniper2 = Sniper('Fridrih Sholtch')

# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 4)
#     sniper1.shoot(sniper2) if choice == 1 or choice == 2 else sniper2.shoot(sniper1)

# if sniper1.health:
#     print(f'{sniper1} won the game!')
# else:
#     print(f'{sniper2} won the game!')

#------------------------------------------

# class Soda:
#     def __init__(self, ingridient=None) -> None:
#         if isinstance(ingridient, str):
#             self.ingridient = ingridient
#         else:
#             self.ingridient = None

#     def __str__(self) -> str:
#         if self.ingridient:
#             return f'gazirovka iz {self.ingridient}'
#         else:
#             return 'normal gazirovka'

# a = Soda('Malina')
# print(a)

# b = Soda(5)
# print(b)

# c = Soda()
# print(c)

# d = Soda('Grusha')
# print(d)

#------------------------------

class TriangleChecker:
    def __init__(self, sides: list[int | float]) -> None:
        self.sides = sides

    def __str__(self) -> str:
        if not all(isinstance(x, (int, float)) for x in self.sides):
            return 'нельзя построить треугольник! инвалид валью!'
        elif any(x <= 0 for x in self.sides):
            return 'нельзя построить треугольник! инвалид валью!'
        self.sides.sort()
        if self.sides[0] + self.sides[1] <= self.sides[-1]:
            return 'нельзя построить треугольник! сумма меньше либо равна!'
        return 'мы можем построить треугольник!'
        
t1 = TriangleChecker([10, 10, 10])
print(t1)
t2 = TriangleChecker([-1, 10, 10])
print(t2)
t3 = TriangleChecker([5, 10, 12])
print(t3)