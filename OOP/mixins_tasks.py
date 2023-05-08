# task 1

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

# task 2

# class RadioMixin:
#     def play_music(self, title):
#         self.title = title
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('Bony M')
# boat.play_music('ABBA')
# obj.play_music('Retro Jazz')

# task 3

# class Clock:
#     from datetime import datetime
#     time_now = datetime.today().strftime("%H:%M:%S")
#     def current_time(self):
#         print(self.time_now)

# class Alarm:

#     def on(self):
#         print('Будильник включен')

#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):

#     def alarm_on(self):
#         self.on()


# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

#task 4

# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass

#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience, languages_backend) -> None:
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, hours):
#         self.hours = hours
#         self.count_code_time += self.hours
           
# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend) -> None:
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, hours):
#         self.hours = hours
#         self.count_code_time += self.hours

# class Fullstack(Backend, Frontend):
#     pass

# a = Backend('Junior', 'Python') 
# b = Frontend('Middle', 'JavaScript') 
# c = Fullstack('Senior', 'Python and JS')
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

# task 5

# class Square:
#     def __init__(self, side) -> None:
#         self.side = side

#     def get_area(self):
#         return self.side * self.side
    
# class Triangle: 
#     def __init__(self, height, base) -> None: 
#         self.height = height 
#         self.base = base 
        
#     def get_area(self): 
#         return int(0.5*self.base*self.height)
    
# class Pyramid(Triangle, Square):
#     def __init__(self, height, base) -> None:
#         super().__init__(height, base)

#     def get_volume(self):
#         return int(1/3*self.base**2*self.height)

# obj = Square(3) 
# print(obj.get_area()) 
# obj2 = Triangle(3,5) 
# print(obj2.get_area()) 
# obj3 = Pyramid(10,10) 
# print(obj3.get_volume()) 

# task 6

# class CreateMixin:
#     def create(self, key, todo): 
#         self.todo = todo
#         self.key = key
#         if key in self.todos.keys(): 
#             return 'Задача под таким ключом уже существует' 
#         else:
#             self.todos[key] = self.todo 
#             return self.todos        

# class DeleteMixin:
#     def delete(self, key):
#         self.key = key
#         if self.key in self.todos:
#             task = self.todos[key]
#             self.todos.pop(key)
#             return task
#         else:
#             return f'нет такого ключа'

# class UpdateMixin:
#     def update(self, key, new_value):
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
#         deadline = datetime.strptime(date, "%d/%m/%Y").date() - datetime.now().date()
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

# task 7

# class ExtensionMixin:
#     def add_extension(self, extension):
#         self.extension = extension
#         self.extensions.append(extension)
#         return f'Добавлено новое расширение {self.extension} для игры {self.name}.'
    
#     def remove_extension(self, extension):
#         self.extension = extension
#         if self.extension in self.extensions:
#             self.extensions.remove(extension)
#             return f'{extension} был отключен от {self.name}'
#         else:
#             return 'Такого расширения нет в списке.'
        
# class Game(ExtensionMixin):

#     def __init__(self, game_type, name) -> None:
#         self.type = game_type
#         self.name = name
#         self.extensions = []

#     def get_description(self, string):
#         self.string = string
#         return f'{self.name} это {self.string}'
    
#     def get_extensions(self): 
#         if len(self.extensions) == 0: 
#             return "Нет подключенных расширений" 
#         else: return self.extensions

# game = Game('CS_GO', 'Minencraft') 
# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром')) 
# print(game.add_extension('Multiverse-Core')) 
# print(game.add_extension('Multiverse-Core1')) 
# game.extensions 
# print(game.get_extensions()) 
# print(game.remove_extension('Multiverse-Core')) 
# print(game.get_extensions())

# task 8

# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class SwimMixin:
#     def swim(self):
#         print('я могу плавать')

# class Human(WalkMixin, SwimMixin):
#     pass

# class Fish(SwimMixin):
#     pass

# class Exocoetidae(FlyMixin, SwimMixin):
#     pass

# class Duck(WalkMixin, FlyMixin, SwimMixin):
#     pass

# human = Human()
# fish = Fish()
# exocoetidae = Exocoetidae()
# duck = Duck()
# human.walk()
# human.swim()
# fish.swim()
# exocoetidae.swim()
# exocoetidae.fly()
# duck.fly()
# duck.swim()
# duck.walk()


    
