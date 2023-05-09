# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class MobilePhone:
#     _battery=100 

#     def __init__(self, imei, os_info) -> None:
#         self._imei = imei
#         self._os_info = os_info

#     def info(self):
#         if self._battery == 0:
#             return f'Телефон разряжен. Зарядите телефон'    
#         elif self._battery >= 0:
#             if self._battery == 0.5:
#                 self._battery -= 0.5
#                 return f'Телефон имеет imei: {self._imei} и на нем установлена ОС: {self._os_info}.\nОстаток заряда составляет: {self._battery}%.\nЗарядите телефон'
#             else:
#                 self._battery -= 0.5
#                 return f'Телефон имеет imei: {self._imei} и на нем установлена ОС: {self._os_info}.\nОстаток заряда составляет: {self._battery}%'
          
#     def listening_to_music(self):
#         if self._battery > 0:
#             if self._battery < 5:
#                 return f'Вы более не можете слушать музыку. Простите. Зарядите телефон.'
#             elif self._battery == 5:
#                 self._battery -= 5
#                 return f'Вы прослушали музыку, но телефон уже разрядился. Заряд батареи: {self._battery}%.\nЗарядите телефон'
#             else:
#                 self._battery -= 5
#                 return f'Приятного прослушивания музыки. Заряд батареи: {self._battery}%'
#         else:
#             return f'Телефон разряжен. Зарядите телефон'

#     def watching_video(self):
#         if self._battery > 0:
#             if self._battery > 10:
#                 self._battery -= 7
#                 return f'Приятного просмотра видео. Заряд батареи: {self._battery}%'
#             else:
#                 return f'Уровень заряда батареи составляет {self._battery}%. При таком заряде нельзя просматривать видео. Зарядите телефон'
#         else:
#             return f'Телефон разряжен. Зарядите его'
        
#     def charge(self):
#         import time
#         count_time = 0
#         while self._battery < 100:
#             if self._battery > 90:
#                 self._battery = 100
#             else:
#                 self._battery += 10           
#             time.sleep(1)
#             count_time += 1
#             print(f'За {count_time} сек заряд составил {self._battery}%')
        
# iphone = MobilePhone('wewe3', 'iOS')
# print(iphone.listening_to_music())
# # print(iphone.listening_to_music())
# # print(iphone.listening_to_music())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.watching_video())
# # print(iphone.listening_to_music())
# # print(iphone.listening_to_music())
# # print(iphone.listening_to_music())
# # print(iphone.listening_to_music())
# # print(iphone.info())
# # iphone.charge()
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # print(iphone.info())
# # iphone.charge()
# # print(iphone.watching_video())


#--------------------------------------

# class Phone:
#     def __init__(self, imei, os) -> None:
#         self.__imei = imei
#         self.__os = os
#         self.__battery_level = 100

#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             raise Exception('Телефон разряжен')
#         print(f'Уровень заряда: {self.__battery_level}')
#         self.__battery_level -= 0.5

#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#            raise Exception('Телефон разряжен')
#         print(f'OS: {self.__imei}, imei: {self.__os}')
#         self.__battery_level -= 0.5

#     @property
#     def play_music(self):
#         if self.__battery_level < 5:
#            raise Exception('Телефон разряжен')
#         print(f'Слушаем музыку')
#         self.__battery_level -= 5

#     @property
#     def play_video(self):
#         if self.__battery_level < 10:
#            raise Exception('Телефон разряжен')
#         print(f'Смотрим видео')
#         self.__battery_level -= 7

#     def charge_battery(self, sec):
#         from datetime import datetime, timedelta
#         from time import sleep

#         now = datetime.now
#         end_time = (now() + timedelta(seconds=sec)).strftime('%M:%S')
#         while now().strftime('%M:%S') != end_time:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level += 5
#             print(f'Идет заряд вашей батареи. Ваш уровень батареи: {self.__battery_level}')

# phone = Phone('123 12313 123', 'iOS 15')
# phone.battery_level
# phone.play_video
# phone.play_music
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.battery_level
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# phone.play_video
# # phone.play_video
# phone.battery_level
# # phone.play_video
# # phone.battery_level
# phone.charge_battery(100)











        



    

