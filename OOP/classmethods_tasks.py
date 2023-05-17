# task 1

# class Product:
#     base_price = 20000

#     def __init__(self, model, year, color) -> None:
#         self.model = model
#         self.year = year
#         self.color = color

#     def has_garantiya(self, year):
#         if (year - self.year) > 2:
#             return 'Ваша гарантия истекла'
#         else:
#             return 'Гарантия действительна'
        
#     @classmethod
#     def change_price(cls, rate):
#         cls.base_price = cls.base_price + (cls.base_price * rate / 100)
#         return cls.base_price

        
# obj = Product('A218', 2008, 'red') 
# obj.change_price(2) 
# print(obj.has_garantiya(2010)) 
# print(obj.base_price) 

# task 2


# class User:

#     def __init__(self, name, lastname, email) -> None:
#         self.name = name
#         self.lastname = lastname
#         self.email = email

#     @staticmethod
#     def validate_email(email):
#         return '@' in email 

#     def __str__(self) -> str:
#         if self.validate_email(self.email):
#             return f'{self.name}: {self.email}' 
#         return "email в неправильном формате" 
        
#     @classmethod
#     def create_user(cls, string):
#         lst = string.split(', ')
#         return User(lst[0], lst[1], lst[2])


# # user1 = User.create_user('John, Snow, john@email.com') 
# # user2 = User.create_user('Jamie, Lanister, john"email.com')
# user1 = User.create_user("Jaanger, Barakanov, jbarakanov@mail.ru")
# user2 = User.create_user("Mars, Radbekov, marsradbek")

# print(user1) 
# print(user2) 

# task 3

# class Makers: 
#     student_count=0 
#     def __init__(self,name,language,kpi): 
#         self.name = name 
#         self.language = language 
#         self.kpi = kpi 

#     @classmethod 
#     def new_student(cls,name,language,kpi): 
#         cls.student_count+=1 
#         return cls(name,language,kpi) 
        
#     def get_info(self): 
#         return f"Student name: {self.name}, Language: {self.language}" 
        
#     def set_kpi(self,kpi): 
#         self.kpi = kpi 
#         return self.kpi 
        
# student1 =Makers.new_student("Marat","JS",'89') 
# student2 =Makers.new_student("Oleg", "Python",'55') 
# print(student1.set_kpi(89)) 
# print(student1.get_info()) 
# print(student2.set_kpi(89)) 
# print(student2.get_info()) 
# print(Makers.student_count)

# task 4

# class Bike:
    
#     def __init__(self, cost, make, model, year, min_profit) -> None:
#         self.cost = cost
#         self.make = make
#         self.model = model
#         self.year = year
#         self._sale_price = None
#         self.sold = False
#         self.min_profit = min_profit

#     def set_cost(self, price):
#         if price >= self.cost:
#             self._sale_price = price
#         else:
#             self._sale_price = price + self.min_profit
        
#     def service(self, cost_repair):
#         self._sale_price += cost_repair
#         return self.cost - self._sale_price
    
#     def sell(self):
#         self.sold = True
#         return self.cost - self._sale_price
    
#     @classmethod
#     def get_default_bike(cls): 
#         return cls(10000, "Author", "Basic ASL", 2020, 2000) 

# bike = Bike.get_default_bike() 
# bike.set_cost(6000) 
# bike.service(300) 
# print(bike.sell()) 
# print(bike.cost) 
# print(bike.make) 
# print(bike.year) 
# print(bike._sale_price) 
# print(bike.sold) 
# print(bike.min_profit) 

# task 5

# class MoneyFmt:

#     def __init__(self, amount) -> None:
#         self.amount = amount

#     @staticmethod
#     def dollarize(float_num: float) -> float:
#         sign = '-' if float_num < 0 else '' 
#         string = sign + '${:,.2f}'.format(abs(float_num)) 
#         return string
    
#     def __str__(self) -> str:
#         return self.dollarize(self.amount)
    
#     def update(self, amount):
#         self.amount = amount

#     def __repr__(self) -> str:
#         return str(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567) 
# print(cash) 
# cash.update(-0.3) 
# print(cash) 
# print(repr(cash)) 




