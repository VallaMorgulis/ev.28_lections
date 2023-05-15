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

# class Student:
#     def __init__(self, name, class_name, ball) -> None:
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball

#     def srednee_znach(self):
#         aver_val = sum(self.ball.values())/len(self.ball)
#         return aver_val

#     def __gt__(self, other): 
#         return f'> {self.srednee_znach() > other.srednee_znach()}' 
    
#     def __lt__(self, other): 
#         return f'< {self.srednee_znach() < other.srednee_znach()}' 
    
#     def __ge__(self,other): 
#         return f'>= {self.srednee_znach() >= other.srednee_znach()}' 
    
#     def __le__(self, other): 
#         return f'<= {self.srednee_znach() <= other.srednee_znach()}' 

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)

# task 5

# class Word:
#     def __init__(self, string) -> None:
#         self.string = string.strip().replace(' ', '')

#     def __gt__(self, other): 
#         return f'{len(self.string) > len(other.string)}' 
    
#     def __lt__(self, other): 
#         return f'{len(self.string) < len(other.string)}' 
    
#     def __ge__(self,other): 
#         return f'{len(self.string) >= len(other.string)}' 
    
#     def __le__(self, other): 
#         return f'{len(self.string) <= len(other.string)}'

# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')  
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2) 

# task 6

# class Kopilka: 
#     def __init__(self): 
#         self.__total = 0 
#         self.__coins = [] 
        
#     def add_moneta(self,moneta): 
#         self.__total += moneta 
#         self.__coins.append(moneta) 
    
#     def __len__(self): 
#         return len(self.__coins) 
    
#     def __getitem__(self,index): 
#         return self.__coins[index] 
    
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30) 

# print(len(obj)) 
# for i in obj: 
#     print(i)



