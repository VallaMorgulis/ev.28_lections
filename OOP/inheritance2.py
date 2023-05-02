# Множественое наследование - это когда класс наслдуется от 2 или более класса

# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')

#     def ride(self):
#         print('We are riding on the graund!')

# class Plane:
#     def play_music_at_station(self):
#         print('Listenind Ed Sheeran')

#     def fly(self):
#         print('We are flying!')
    
# class FutureAuto(Plane, Auto):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()


# print(dir(object))

#-----------------------

# Проблема ромба - когда поиск шел в родитесльский класс прежде чем искать у соседнего общего потомка (решена с помощью MRO)
# MRO (Method Resolution Order)- механизм для корректного поиска родительских методов. Был создан для решения проблемы ромба, которая появилась после введения object в пайтоне. Поиск идет таким образомчто если у родительских классов есть общий предок, то идет поиск в ширину.

# class Zero:
#     def say(self):
#         print('class Zero')

# class First(Zero):
#     def say(self):
#         print('class First')

# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('class MyClass')

# obj = MyClass()
# obj.say()
# print(MyClass.mro())



# class Z:#3
#     pass

# class Y:#5
#     pass

# class A(Z):#2
#     pass

# class B(Y):#4
#     pass

# class X(A, B): #1
#     pass

# print(X.mro())


# Проблема перекресного наследования

# class Y:
#     pass

# class X:
#     pass

# class A(Y, X):
#     pass

# class B(X, Y):
#     pass

# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]

# class MyClass(A, B, metaclass=MyMro):
#     pass

# print(MyClass.mro())


