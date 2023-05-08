# анатоция свойств(@property(getter setter))

# class Person:
#     __name = 'John'
#     __age = 22
#     __code = '+996'
#     __number = '555666777'
#     __full_number = __code + __number

#     @property
#     def name(self):
#         '''The name property(getter)'''
#         print(self.__name)
#         return (self.__name)

#     @name.setter
#     def name(self, value):
#         if not isinstance(value, str):
#             print('Invalid value for name')
#         else:
#             self.__name = value
#             print('Setter', value)

#     @property
#     def age(self):
#         print(self.__age)
#         return self.__age

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0, 150):
#             print('Invalid values!')
#         else:
#             self.__age = value

#     @property
#     def number(self):
#         name = input('Vvedite svoe imia: ')
#         if self.__name.lower().strip() != name.lower().strip():
#             print('Invalid name!')
#         else:
#             print(self.__full_number)

#     @number.setter
#     def number(self, value: dict):
#         '''Value must be dict, first pair cod, second pair number'''
#         if value['code'] != '+996':
#             print('number changed from Kyrgyzstan number!')
#         elif len(value['number']) != 9:
#             print('number changed from Kyrgyzstan number!')
#         self.__code = value['code']
#         self.__number = value['number']
#         self.__full_number = self.__code + self.__number
#         print(self.__full_number)


    



            
# obj = Person()
# obj.name
# obj.name = "Jamie"
# obj.name
# obj.age
# obj.age = 30
# obj.age
# obj.number
# obj.number = {'code': '+7', 'number':'777888999'}
# obj.number

#-----------------------

# read - write - delete (radius)

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     def _get_radius(self):
#         print('getter, _get_radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('setter, _set_radius')
#         if not isinstance(value, (int,float)):
#             raise ValueError('radius must be an int or float object!')
#         self._radius = value

#     def _del_radius(self):
#         print('deleter, _del_radius')
#         answer = input('Are you sure to delete radius(y/n)? ')
#         if answer.lower().strip() == 'y':
#             del self._radius
#             print('Deleted')
#         else:
#             print('Not deleted!')
        
#     radius = property(fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc='The radius property')

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7
# print(obj.radius)
# del obj.radius
# print(obj.radius)


# a = 5
# print(a)
# del a
# print (a)

# class A:
#     test = 5

# obj = A
# print(obj.test)
# del A.test
# print(obj.test)

# ----------------------------
# read only

# class CoordinateWriteError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y) -> None:
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         print(self.__x)

#     @property
#     def y(self):
#         print(self.__y)

#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError('x coordinate is read only field')
    
#     @y.setter
#     def y(self, value):
#         raise CoordinateWriteError('x coordinate is read only field')


# obj = Point(42, 74)
# obj.x
# obj.y

#-----------------------
#write only

# import hashlib
# import os

# class User:
#     def __init__(self, username, password) -> None:
#         self.username = username
#         self.password = password

#     @property
#     def password(self):
#         raise AttributeError('Password field is write-only')
    
#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str):
#             raise ValueError('Invalid value for password!')
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256', value.encode('utf-8'), salt, 100_000)

# john = User('JohnSnow', 'secretkey')
# # print(john.password)
# john.password = 'johnthebest'
# print(john._hashed_password)

