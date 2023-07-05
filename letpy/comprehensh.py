# enter_words = input()
# list_ = enter_words.split(' ')
# words = [x for x in list_ if x.isalnum()]
# speach = ' '.join(words)
# print(speach)

#-----------------------------------------

# enter_text = input()
# list_ = enter_text.split(' ')
# numbers = sorted([int(x) for x in list_ if x.isdigit()])
# print(numbers)

# --------------------------------------

# from random import shuffle

# tasks = []

# while True:
#     task = input()
#     if not task:
#         break
#     else:
#         tasks.append(task)

# shuffle(tasks)
# for task in tasks:
#     print(task)

#----------------------------------

# from random import choice

# symbols = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# length = int(input())
# password = ''.join([choice(symbols) for x in range(length)])
# print(password)

#-----------------------------------

# # импортируем tkinter
# import tkinter
# # создаем окно
# window = tkinter.Tk()
# # создаем холст и размещаем его в окне
# canvas = tkinter.Canvas(window)
# canvas.pack()

# for i in range(5, 100, 5):
#     # 1 вариант вывода через if else 
#     if i % 2 == 0: 
#         canvas.create_oval(100-i, 100-i, 100+i, 100+i, outline="red")
#     else: 
#         canvas.create_oval(100-i, 100-i, 100+i, 100+i, outline="grey")
#     # 2 вариант вывода через терр оператор if else при выборе цвета 
#     canvas.create_oval(200-i, 100-i, 200+i, 100+i, outline=("green" if i % 2 == 0 else "cyan"))


# window.mainloop()

#----------------------------

# import time
# import random
# import tkinter
# window = tkinter.Tk()
# canvas = tkinter.Canvas(window, width=400, height=400)
# canvas.pack()
# colors = ('azure3', 'chocolate3', 'dark red', 'DarkOrchid', 'deep pink', 'goldenrod', 'LawnGreen')
# while True:
#     x = random.randint(0, 400)
#     y = random.randint(0, 400)
#     for i, e in enumerate(range(150, 181, 5)):
#         canvas.create_oval(x - e, y - e, x + e, y + e, outline = colors[i])
#         canvas.update()
#         time.sleep(0.05)
# window.mainloop()

#---------------------------------

# from random import randint

# number = randint(0, 10)
# print(number)
# flag = False
# for attempt in range(3):
#     num = int(input())
#     if num < number:
#         print('Загаданное число меньше')
#     elif num > number:
#         print('Загаданное число больше')
#     elif num == number:
#         print('Вы выиграли')
#         flag = True
#         break

# if flag == False:
#     print('Вы проиграли')




# from random import randint
# number = randint(0,10)
# count = 0
# for i in range(3):
#     res = int(input('Введите загаданноое число: '))
#     if res < number:
#         print('Загаданное число больше')
#         count += 1
#     elif res > number:
#         print('Загаданное число меньше')
#         count += 1
#     elif res == number:
#         print('Вы выиграли')
#         break
# if count == 3:
#     print("Вы проиграли")


a = [1, 2, 3]
b = a[:]
print(id(a), id(b))