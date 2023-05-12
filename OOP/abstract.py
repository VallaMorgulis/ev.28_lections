'''
Абстракция
'''

# Абстракция (Абстрактный класс) - принцип ООП, в котором создается абстрактный класс (класс - пустышка), в котором создаются названия атрибутов и методов, для того, чтобы мы могли их переопределить в дочерних классах нужным образом. (Есть названия, но нет логики)

# from abc import ABC, abstractmethod, abstractproperty

# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         ...

#     @abstractproperty
#     def legs(self):
#         ...

# @abstractmethod - декоратор который требует  переопределения метода в наследуемом классе
# @abstractproperty - декоратор который требует переопределение аттрибутов класса
# obj = AbstractAnimal() #TypeError: Can't instantiate abstract class AbstractAnimal with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     ...

# obj = Dog() #TypeError: Can't instantiate abstract class Dog with abstract methods legs, voice

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('гав-гав')

    # def legs(self):
    #     return 4

# obj = Dog()
# obj.voice()
# print(obj.legs)

# class Cat(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('Meow')

# dog = Dog()
# cat = Cat()
# arr = [dog, cat]
# for i in arr:
#     i.voice()
#     print(i.legs)


# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         ...

# class Square(Shape):
#     def __init__(self, length) -> None:
#         self.lehgth = length

#     def area(self):
#         return self.lehgth ** 2

# obj = Square(12)
# print(obj.area())


