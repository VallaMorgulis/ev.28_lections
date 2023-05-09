# class  methods, instance methods, static methods

# instance methods - это у нас обычные методы, которые первым аргуменом принимает self (ссылка на объект). Нужны, чтобы внутри метода работать мы могли работать с аргументами объекта, получать их или изменять их.

# class Test:
#     def instance_method(self, a):
#         print('метод объекта')
#         print('первый аргумент:', self)
#         self.attribute = 5

# obj = Test()
# obj1 = Test()
# obj.instance_method(5) # если вызвать у объекта, то в self передается автоматически
# Test.instance_method(obj, 5) # если вызвать у класса, то в self нуно передать объект вручную
# obj1.instance_method(5)

# class methods - метобы, которые принимают первым аргцментом cls(ссылка на класс). Нужны они для создания или изменения аттрибутов класса и для манипуляции с классом внутри метода. Создаетcя при помощи декоратора класс метод @classmethod.

# class Test:
#     @classmethod
#     def class_method(cls, a):
#         print('метод класса')
#         print('первый аргумент', cls)

# obj = Test()
# print(Test, '!!!')
# print()
# obj.class_method(5)
# print()
# Test.class_method(5)

# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self.a = 4

# obj_1 = C()
# obj_2 = C()
# obj_3 = C()

# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_2.counter)
# obj_1.counter += 1
# print()
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_2.counter)
# print()
# C.counter += 5
# print('obj_1', obj_1.counter)
# print('obj_2', obj_2.counter)
# print('obj_3', obj_2.counter)



# class C:
#     counter = 0

#     def __init__(self) -> None:
#         self._inc_counter()
#         self.a = 4

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1


# obj1 = C()
# obj2 = C()
# obj3 = C()
# print(obj3.counter)
# obj4 = C()
# print(obj1.counter)
# print(obj2.counter)
# print(obj3.counter)
# print(obj4.counter)



# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print(f'Готовиться пицца размером {self.r * 2} см')

#     @classmethod
#     def four_cheese(cls, r):
#         pizza = cls(r, 'моцарелла', 'голландский', 'дорблю', 'брынза')
#         return pizza
    
#     def __str__(self) -> str:
#         return f'{self.r} cm -> ' + ', '.join(self.ingredients)


# pizza1 = Pizza(20, 'пеперони', 'грибы', 'мацарелла')
# print(pizza1.cook())
# # pizza2 = Pizza(15, 'моцарелла', 'голландский', 'дорблю', 'брынза')
# # pizza3 = Pizza(20, 'моцарелла', 'голландский', 'дорблю', 'брынза')
# # pizza4 = Pizza(10, 'моцарелла', 'голландский', 'дорблю', 'брынза')
# pizza2 = Pizza.four_cheese(15)
# pizza3 = Pizza.four_cheese(10)
# pizza4 = Pizza.four_cheese(20)
# pizza5 = Pizza(20, 'пеперони', 'грибы', 'мацарелла', 'оливки')
# print(pizza1)
# print(pizza2)
# print(pizza3)
# print(pizza4)
# print(pizza5)

# class Person:
#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Name: {self.name} {self.surname} -> Age: {self.age}')

#     @classmethod
#     def from_birth_year(cls, name, birth_date):
#         from datetime import date
#         age = date.today().year - birth_date
#         return cls(name, age)

# obj = Person('John', 24)
# obj.info()
# obj2 = Person('Sansa', 19)
# obj2.info()
# obj3 = Person.from_birth_year('Rob', 1996)
# obj3.info()
    
# from datetime import datetime, date
# a = datetime.now()
# print(a.strftime('%H:%M:%S'), type(a))

# staticmethod - это те методы в классе, которые не принимают в качестве агрументов ни класс, ни объект, так называемые методы, которые не изменяют состояние.

# class C:
#     @staticmethod
#     def static_method(a):
#         print('статический метод')
#         print(a)

# obj = C()
# obj.static_method(5)
# C.static_method(5)

class Cylinder:
    def __init__(self, radius, height) -> None:
        self.area = self.get_area(radius, height)
        
    @staticmethod
    def get_area(r, h):
        from math import pi
        circle2 = (pi * r ** 2) * 2
        side = 2 * pi * r * h
        area = circle2 + side
        return round(area, 2)


obj = Cylinder(10, 7)
print(f'Area: {obj.area}')
print()
obj1 = Cylinder(3, 12)
print(f'Area: {obj1.area}')


