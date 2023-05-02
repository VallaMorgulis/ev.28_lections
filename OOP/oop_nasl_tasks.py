# task 1

# class Class1:
    
#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):

#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())

# task 2

# class A:
    
#     def method1(self):
#         print('Основной функционал')

# class B(A):
    
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# task 3

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
# print(example.pop()) 
# print(example) 

# task 4

# class MyDict(dict): 
#     def get(self,key,default = 'Are you kidding?'): 
#         return dict.get(self,key,default) 
    
# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

# task 5

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'name:{self.name}, age:{self.age}'

# class Student(Person):
     
#     def __init__(self, name, age, faculty) -> None:
#          super().__init__(name, age)
#          self.faculty = faculty

#     def display_student(self):
#         person_info = super().display()
#         return f'{person_info}, faculty:{self.faculty}'

# obj_student = Student('Rick', '21', 'science')
# print(obj_student.display() )
# print(obj_student.display_student())
    
# task 6

# class ContactList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         self.name = name
#         coincidences = [x for x in self.list_ if self.name in x]
#         return coincidences

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

# task 7

# class SmartPhones:

#     def __init__(self, name, color, memory, battery=0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def __str__(self) -> str:
#         return f'{self.name} {self.memory}'
    
#     def charge(self, charge_units):
#         self.battery += charge_units
#         return self.battery
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios, send_imessage='', battery=0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.ios = ios
#         self.send_mess = send_imessage

#     def send_imessage(self, string):
#         self.string = string
#         return f'sending {self.string} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
    

#     def __init__(self, name, color, memory, android, show_time=None, battery=0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.android = android
#         self.time_now = show_time

#     def show_time(self):
#         import datetime
#         vremya = datetime.datetime.now().time()
#         return vremya

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone)
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

# task 8

# class CustomError(Exception): 
#     def __init__(self, message): 
#         self.message = message 
        
# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ') 

# def check_letters(message1): 
#     if message1 == message1.upper():
#         return f'ВСЕ ОТЛИЧНО! {message1}' 
#     else: 
#         raise capitals_error 
    
# print(check_letters("HELLO"))


# task 1

# class Class1:

#     def __init__(self) -> None:
#         pass

#     def first(self):
#         pass

#     def second(self):
#         pass

# class Class2(Class1):

#     def __init__(self) -> None:
#         pass

#     def third(self):
#         pass

#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()

# task 2

# class A:

#     def method1(self):
#         print('Основной функционал')

# class B(A):

#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# task 3

# class MyString(str):

#     def __init__(self, str1) -> None:
#         self.str1 = str1

#     def append(self, str2):
#         self.str2 = str2
#         self.str1 = self.str1 + self.str2
#         return self.str1
    
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

# task 4

# class MyDict(dict):

#      def get(self,key,value = 'Are you kidding?'): 
#        return dict.get(self,key,value) 

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some_title'))

# task 5

# class Person:

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display(self):
#         return f'name:{self.name}, age:{self.age}'
    
# class Student(Person):

#     def __init__(self, name, age, faculty) -> None:
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         person = super().display()
#         return f'{person}, faculty:{self.faculty}'
    
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())

# task 6

# class ContactList(list):

#     def __init__(self, list_):
#         self.list_ = list_

#     def search_by_name(self, name):
#         self.name = name
#         list_same = [x for x in self.list_ if self.name in x]
#         return list_same


# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya')) 

# task 7

# class SmartPhones:

#     def __init__(self, name, color, memory, battery=0) -> None:
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def __str__(self):
#         return f'{self.name} {self.memory}'
    
#     def charge(self, pers):
#         self.pers = pers
#         self.battery += pers
#         return self.battery
    
# class Iphone(SmartPhones):

#     def __init__(self, name, color, memory, ios, battery=0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.ios = ios

#     def send_imessage(self, string):
#         self.string = string
#         return f'sending {self.string} from {self.name} {self.memory}'
    
# class Samsung(SmartPhones):

#     def __init__(self, name, color, memory, android, battery=0) -> None:
#         super().__init__(name, color, memory, battery)
#         self.android = android

#     def show_time(self):
#         from datetime import datetime
#         current_time = datetime.now().time()
#         return current_time
    
# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 
# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery)
# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello')) 
# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())

# task 8

# class CustomError(Exception):

#     def __init__(self, capitals_error: object) -> None:
#         self.message = capitals_error


# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_ == str_.upper():
#         return f'ВСЕ ОТЛИЧНО! {str_}' 
#     else: 
#         raise capitals_error
    
# print(check_letters("HELLO"))




