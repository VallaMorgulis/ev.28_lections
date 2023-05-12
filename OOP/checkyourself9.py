# class CreateMixin:
#     def create(self, key: int, todo: str) -> dict: 
#         self.todo = todo
#         self.key = key
#         if key in self.todos.keys(): 
#             return 'Задача под таким ключом уже существует' 
#         else:
#             self.todos[key] = self.todo 
#             return self.todos        

# class DeleteMixin:
#     def delete(self, key: int) -> str:
#         self.key = key
#         if self.key in self.todos:
#             task = self.todos[key]
#             self.todos.pop(key)
#             return task
#         else:
#             return f'нет такого ключа'

# class UpdateMixin:
#     def update(self, key: int, new_value: str) -> dict:
#         self.key = key
#         self.new_value = new_value
#         if key in self.todos.keys():
#             item = {key: new_value}
#             self.todos.update(item)
#             return self.todos
#         else:
#             return f'нет такого ключа'

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, date):
#         self.date = date
#         from datetime import datetime
#         deadline = datetime.now().date() - datetime.strptime(date, "%d/%m/%Y").date()
#         return int(deadline.days)
    
# task = ToDo()
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))
# print(task.todos)


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


# class A:
#     def count(self, ):


# class B:
#     pass

# from abc import ABC, abstractmethod

# class Planet(ABC):
#     def __init__(self, orbit): 
#         self.orbit = orbit
    
#     @abstractmethod
#     def get_age(self, earth_age):
#         ...

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


# from abc import ABC, abstractmethod
   
# class Fauna(ABC):
#     @abstractmethod
#     def fly(self):
#         ...

#     @abstractmethod
#     def grow(self):
#         ...
        
#     @abstractmethod    
#     def sound(self):
#         ...

# class Bird(Fauna):
#     def fly(self):
#         print('я лечу')

#     def grow(self):
#         print('я расту')
        
#     def sound(self):
#         print('я пою')

# class Animal(Fauna):
#     def fly(self):
#         print('я лечу')

#     def grow(self):
#         print('я расту')
        
#     def sound(self):
#         print('я пою')

  
# class Plant(Fauna):
#     def grow(self):
#         print('я расту')
        
#     def photosynthesize(self):
#         print('я на солнце')

#     def fly(self): # если закоментить, то вылетит ошибка, т.к. абстрактный класс не даст оставить безучастным сие вопиющие нарушение этикета.
#         ...

#     def sound(self):# если закоментить, то вылетит ошибка, т.к. абстрактный класс не даст оставить безучастным сие вопиющие нарушение этикета.
#         ...

# animal = Animal()
# bird = Bird()
# plant = Plant()
# animal.fly()
# animal.grow()
# animal.sound()
# bird.fly()
# bird.grow()
# bird.sound()
# plant.fly()
# plant.grow()
# plant.sound()
# plant.photosynthesize()

# from abc import ABC, abstractmethod

# class Letters(ABC):
#     @abstractmethod
#     def count(self):
#         ...

# class A:
#     def __init__(self, string) -> None:
#         self.string = string

#     def count(self):
#         gl = [x for x in self.string if x.lower() in ['e','u','i','o','a','y']]
#         return len(gl)

# class B:
#     def __init__(self, string) -> None:
#         self.string = string

#     def count(self):
#         sogl = [x for x in self.string if x.lower() in ['q','w','r','t','p','s','d','f','g','h','j','l','z','x','c','v','b','n','m','k']]
#         return len(sogl)
    
# a = A('Makers')
# b = B('Makers')
# c = A('Boopcamp')
# d = B('Boopcamp')
# list_ = [a, b, c, d]
# res = [x.count() for x in list_]
# print(res)


"""
1) # Напишите класс CustomNumber, который принимает одно число и будет выполнять ту или иную операцию с ним.
# Перезапишите магические методы этих операторов
# Оператор сложения (+) будет выполнять функцию оператора  вычитания (-) и наоборот
# Оператор умножения (*) будет выполнять функцию оператора деления (/) и наоборот
# Так же перезапишите функционал операторов сравнения на противоположные (>, < ,==, !=)

# Вывод:
# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 5
# print(num2 - num1)  # 15
# print(num1 * num2)  # 2.0
# print(num2 / num1)  # 0.5

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # False
# print(num1 < num2)   # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True


"""

# class CustomNumber(int):
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         instance = super().__new__(cls)
#         instance.number = number
#         return instance
    
#     def __add__(self, other):
#         res = self.number - other.number
#         return res

#     def __sub__(self, other):
#         res = self.number + other.number
#         return res
    
#     def __mul__(self, other):
#         res = self.number / other.number
#         return res

#     def __truediv__(self, other):
#         res = self.number * other.number
#         return res
    
#     def __gt__(self, other) -> bool:
#         return self.number < other.number
    
#     def __eq__(self, other) -> bool:
#         return self.number != other.number
    
#     def __le__(self, other) -> bool:
#         return self.number >= other.number
    
#     def __lt__(self, other) -> bool:
#         return self.number > other.number
    
#     def __ne__(self, other) -> bool:
#         return self.number == other.number
    
#     def __ge__(self, other) -> bool:
#         return self.number <= other.number
    
# num1 = CustomNumber(10)
# num2 = CustomNumber(5)

# print(num1 + num2)  # 5
# print(num2 - num1)  # 15
# print(num1 * num2)  # 2.0
# print(num2 / num1)  # 50

# print(num1 == num2)  # False
# print(num1 != num2)  # True
# print(num1 > num2)   # False
# print(num1 < num2)   # True
# print(num1 >= num2)  # False
# print(num1 <= num2)  # True   
 
 
    


