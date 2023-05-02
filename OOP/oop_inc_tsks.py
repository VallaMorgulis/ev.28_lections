#task 1

# class A: 
#     def public(self): 
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'

# obj1 = A() 
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

# task 2

# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     def __init__(self) -> None:
#         super().__init__()

# b1 = B()
# b1.method1()

# task 3

class Car:
    def __init__(self) -> None:
        self.__speed

    def set_speed(self, new):
        self.__speed = new

    def show_speed(self):
        return self.__speed
    
car1 = Car() 
print(car1.show_speed()) 
car1.set_speed(20) 
print(car1.show_speed()) 



