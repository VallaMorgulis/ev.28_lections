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
#         # print(f'{self.time_now.hour}:{self.time_now.minute}:{self.time_now.second}')
#         print(self.time_now)

# class Alarm:

#     def on(self):
#         pass

#     def off(self):
#         pass

# class AlarmClock(Clock, Alarm):

#     def alarm_on(self):
#         print('Будильник включен')


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






