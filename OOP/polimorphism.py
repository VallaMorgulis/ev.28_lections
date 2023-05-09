# функция полиморфизма - len(): __len__
# print(len('Makers'))
# print(len([1,2,3,4]))
# print(len({1:2, 4:5}))

# + (__add__) - метод полиморфизм
# print(5 + 5)
# print('hello' + 'hello')
# print([1,2,3] + [4,5,6])

# Полиморфизм - это способность функции/метода использоваться для разных типов (классов)
# Широко распространненое определение: "один интерфейс - много реализаций"
# list.pop()
# set.pop()
# dict.pop()

# class Cat:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Meow, meow')

# class Dog:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dogs name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('Bark, bark')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()


# from math import pi

# class Shape:

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

