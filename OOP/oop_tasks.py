# task 1

# class Song():

#     def __init__(self, title, author, year): 
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Monaco','Chebotina', '2018')
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# task 2

# class Circle:
#     color = 'синий'
#     pi = 3.14

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def get_area(self):
#         return self.pi * self.radius ** 2
    
# circle = Circle(2)
# circle.color = 'красный'
# print(circle.color)
# print(circle.get_area())

# task 3

# class BankAccount:
#     balance = 0

#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000) 
# account.withdraw(500) 

# task 4

# class Taxi:

#     def __init__(self, name, cost, cost_km) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         return f'Такси {self.name}, стоимость поездки: {km * self.cost_km + self.cost} сом'
     



# taxi1 = Taxi('Namba', 50, 1.5)
# taxi2 = Taxi('Yandex', 40, 1.4)
# taxi3 = Taxi('Jorgo', 60, 1.7)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))

# task 5

# class Phone:

#     def __init__(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', '+996707707707')
# contact.get_info()

# task 6

# class Salary:

#     percent = 8

#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return self.salary * (self.percent / 100) * self.experience


# obj = Salary(10000, 10)
# print(obj.count_percent())

# task 7

# class Nobel:
#     from datetime import datetime
#     now = datetime.now()

#     def __init__(self, category, year, winner) -> None:
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         res = self.now.year - self.year
#         return f'выиграл {res} лет назад'



# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# task 8

# class Password:

#     def __init__(self, password): 
#         self.password = password

#     def __str__(self) -> str:
#         return '*' * len(self.password)

#     def validate(self):
#         if len(self.password) == 8 and len(self.password) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         elif not any(map(lambda x: x.isdigit()), self.password):
#             return f'Password should contain numbers too'
#         elif not any(map(lambda x: x.isalpha()), self.password):
#             return f'Password should contain letters as well'
#         elif not any(map(lambda x: x in ['@', '#', '&', '$', '%', '!', '~', '*'], self.password)):
#             return f'Your password should have some symbols'
#         return f'Ваш пароль сохранен.'     

 
        
# passw = Password('Ert2ewew')
# print(passw.validate())
# print(passw)

# task 9

# class Math:

#     def __init__(self, number) -> None:
#         self.number = number

#     def get_factorial(self):
#         factorial = 1
 
#         for i in range(2, self.number+1):
#             factorial *= i
#         return factorial

#     def get_sum(self):

#         num_list = [int(x) for x in str(self.number)]
#         suma = sum(num_list)
#         return suma
        
#     def get_mul_table(self): 
#         str_ = ''
#         for i in range(1, 11):
#             str_ = str_ + f'{self.number} x {i} = {self.number * i}\n'
#         return str_
    
# num_ = Math(11)
# print(num_.get_factorial())
# print(num_.get_sum())
# print(num_.get_mul_table())

# task 10

# class ToDo:
#     instances = {}

#     def __init__(self, string) -> None:
#         self.string = string

#     def give_priority(self, priority: int):
#         self.instances[priority] = self.string
        
#     def list_of_tasks(self):
#         return sorted(ToDo.instances.items())

# us1 = ToDo('Сходить в школу')
# print(us1.string)
# us1.give_priority(1)
# print(ToDo.instances)
# us1 = ToDo('Поесть суши')
# us1.give_priority(3)
# print(ToDo.instances)
# print(us1.list_of_tasks())



# task 1

# class Song:

#     def __init__(self, title, author, year) -> None:
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'

# song = Song('Happy', 'Pharrell Williams', 2013)
    
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# task 2

# class Circle:
#     color = 'Синий'
#     pi = 3.14

#     def __init__(self, radius) -> None:
#         self.radius = radius

#     def get_area(self):
#         return self.pi * self.radius ** 2

# circle = Circle(2) 
# circle.color = 'Красный'
# print(circle.color)
# print(circle.get_area())

# task 3

# class BankAccount:
#     def __init__(self, balance=0) -> None:
#           self.balance = balance

#     def withdraw(self, amount):
#         self.amount = amount
#         self.balance -= self.amount
#         print(f'Ваш баланс: {self.balance} сом')
    
#     def deposit(self, amount):
#         self.amount = amount
#         self.balance += self.amount
#         print(f'Ваш баланс: {self.balance} сом')
    
# account = BankAccount()
    
# account.deposit(1000)
# account.withdraw(500)

# task 4

# class Taxi:

#     def __init__(self, name, cost, cost_km) -> None:
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km

#     def get_total_cost(self, km):
#         self.km = km
#         result = self.km * self.cost_km + self.cost
#         return f'Такси {self.name}, стоимость поездки: {result} сом' 
    
# taxi1 = Taxi('Namba', 50, 1.5) 
# taxi2 = Taxi('Yandex', 60, 1.4) 
# taxi3 = Taxi('NamJorgoba', 30, 1.7)    
    
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))  

# task 5

# class Phone:
    
#     def __init__(self, name, last_name, phone) -> None:
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John', 'Snow', +996707707707)
# contact.get_info()

# task 6

# class Salary:
#     percent = 8

#     def __init__(self, salary, experience) -> None:
#         self.salary = salary
#         self.exp = experience

#     def count_percent(self):
#         return self.salary * self.exp * (self.percent / 100)
    

# obj = Salary(10000, 10)
# print(obj.count_percent()) 

# task 7

# class Nobel:
#     from datetime import datetime
#     now = datetime.now()

#     def __init__(self, category, year, winner) -> None:
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         res = self.now.year - self.year
#         return f'выиграл {res} лет назад' 

# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

  
# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# task 8

# class Password:

#     def __init__(self, password) -> None:
#         self.passw = password

#     def validate(self):
#         if len(self.passw) == 8 and len(self.passw) < 15:
#             return f'Password should be longer than 8, and less than 15'
#         elif not any(list(map(lambda x: x.isdigit(), self.passw))):
#             return f'Password should contain numbers too'
#         elif not any(list(map(lambda x: x.isalpha(), self.passw))):
#             return f'Password should contain letters as well'
#         elif not any(list(map(lambda x: x in ['@', '#', '&', '$', '%', '!', '~', '*'], self.passw))):
#             return f'Your password should have some symbols'
#         else:
#             return f'Ваш пароль сохранен.'

#     def __str__(self) -> str:
#         return "*" * len(self.passw)
    
# password = Password('joe@123456')
# print(password.validate())
# print(password)

# task 9

# class Math:

#     def __init__(self, number) -> None:
#         self.num = number

#     def get_factorial(self):
#         import math
#         return math.factorial(self.num)

#     def get_sum(self):
#         return sum([int(x) for x in str(self.num)])

#     def get_mul_table(self):
#         res = ''
#         for x in range(1, 11):
#             res = res + f'{self.num} x {x} = {self.num * x}\n'

#         return res
    
# obj = Math(11)
# print(obj.get_factorial())
# print(obj.get_sum())
# print(obj.get_mul_table())

# task 10

# class ToDo:
#     instances = {}

#     def __init__(self, str_) -> None:
#         self.str_ = str_

#     def give_priority(self, priority):
#         self.priority = priority
#         self.instances[priority] = self.str_
#         return self.instances
    
#     def list_of_tasks(self):
#         list_ = [x for x in self.instances.items()]
#         return sorted(list_)
    
# user = ToDo('Go to shop')
# print(user.give_priority(2))
# print(user.list_of_tasks()) 
















        
    



    

    






