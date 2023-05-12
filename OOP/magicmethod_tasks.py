# task 1

# class Account:
#     def __init__(self, name, balance, city) -> None:
#         self.name = name
#         self. balance = balance
#         self.city = city
#         print('Счет создан')

#     def __repr__(self) -> str:
#         return f'{self.name} {self.balance}'
    
#     def __str__(self) -> str:
#         return f'Hello {self.name} {self.balance} {self.city}'
    
#     def __del__(self):
#         print('Пока')

# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account))

# task 2

# class MyNumber(int):
#     def __init__(self, value) -> None:
#         super().__init__()
#         self.value = value

#     def __add__(self, other):
#         x = self.value + other
#         return f'Это сложение и результат равен: {x}'

#     def __sub__(self, other):
#         x = self.value - other
#         return f'Это вычитание и результат равен: {x}'
    
#     def __mul__(self, other):
#         x = self.value * other
#         return f'Это умножение и результат равен: {x}'

#     def __truediv__(self, other):
#         x = self.value / other
#         return f'Это деление и результат равен: {x}'
    
# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)

# task 3

# class MyList(list):
#     def __init__(self, item):
#         super().__init__()
#         self.item = item
#     def __getitem__(self, index):
#         return self.item[index - 1]
    
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1])

# task 4

class Student:
    def __init__(self, name,  class_name, ball) -> None:
        self.name = name
        self.class_name = class_name
        self.ball = {}

#     def count_balls(self, other):
#         a = (sum([x for x in self.ball.values()])) / len(self.ball)
#         b = (sum([x for x in other.ball.values()])) / len(other.ball)

    def __gt__(self, other) -> bool:
        a = (sum([x for x in self.ball.values()])) / len(self.ball)
        b = (sum([x for x in other.ball.values()])) / len(other.ball)
        return a > b
    
#     def __le__(self, other) -> bool:
#         self.count_ball()
#         return a <= b
    
#     def __lt__(self, other) -> bool:
#         self.count_ball()
#         return a < b
    
#     def __ge__(self, other) -> bool:
#         self.count_ball()
#         return a >= b
    

obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
print(obj_student1 > obj_student2)  
# print(obj_studen 1 <= obj_student2)


# a = {'math': 100, 'history': 50, 'literature': 88}
# b = a['math'] + a['history'] + a['literature']

# b = (sum([x for x in a.values()])) / len(a)
# print(b)

    
    


