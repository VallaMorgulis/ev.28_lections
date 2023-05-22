# task 1

# class MyString(str):

#     def __init__(self, str1): 
#          self.str1 = str1

#     def append(self, str2):
#        self.str2 = str2
#        self.str1 = self.str1 + self.str2
#        return self.str1

#     def pop(self):
#         last_simbol = self.str1[-1]
#         self.str1 = self.str1[:-1]
#         return last_simbol
    
#     def __str__(self) -> str: 
#         return self.str1 
    
# example = MyString('String')
# example.append('hello')
# print(example)
# print(example.pop()) 
# print(example)

# task 2

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

# task 3

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

# task 4

from random import randint
 
class Person:
    def __init__(self, col):
        self.id = randint(0, 100)
        self.command_hero = col

    def __str__(self) -> str:
        return self.command_hero
 
class Heroes(Person):
    level = 1

    def level_up(self):
        self.level += 1
        print('герой с id ' + str(self.id) +' достиг второго уровня')

    def create_heroes(self):
        return self.command_hero + '_Hero'   
        # list_heroes = []
        # for hero in range(1,3):
        #     res = str(hero) + '_Hero'
        #     list_heroes.append(res)
        # return list_heroes
    
    def create_solders(self):
        list_solders = [(self.create_heroes() + '_Soldier' + str(randint(2, 35))) for x in range(1,6)]
        return list_solders
 
class Soldiers(Person):
    def __init__(self):
        Person.__init__(self, col = 1)

    def going_to_hero(self, list_solders):
        ...


hero_blue = Heroes('Blue')
hero_red = Heroes('Red')
print(hero_blue)
print(hero_blue.create_heroes())
print(hero_red.create_heroes())
print(hero_blue.create_solders())
print(hero_red.create_solders())
hero_red.level_up()






