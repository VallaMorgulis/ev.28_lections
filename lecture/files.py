# работа с файлами

# каретка - указатель - курсор

# open(<путь до файла>)

# file = open('/home/valla/Desktop/ev.28/lecture') # абсолютный путь

# file = open('files.py') # относительный путь (отгосительно той директории в которой вы работаете)

# режимы работы с файлами
# 1. чтение -> r/r+ (read)
# 2. записи -> w/w+ (write)
# 3. добавление -> a/a+ (append)
# b, x, t

# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# file = open('text.txt')
# data = file.read()
# data = data.split('\n')
# print(data)
# file.close()

# контекстный менеджер

# with open('text.txt') as file:   # file = open('text.txt')
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())
#     print(file, 'inside')

# print(file, 'outside')

# file.tell() -> возвращает индекс где находится каретка (указатель или курсор)
# file.seek(index) -> перемещает курсор на индекс, который вы передали

# with open('text.txt', 'r') as file:
    # print(file.readline().replace('\n', ''))
    # print(file.tell())
    # file.seek(0)
    # print(file.readline().replace('\n', ''))
    # data = file.read()
    # index = data.index('\n')
    # file.seek(index+1)
    # print(file.readline().replace('\n', ''))
    # print(file.readlines()[2])
    # print(file.tell())
    # file.read()
    # file.seek(0)
    # print(file.tell())
    # print(file.readline())

# with open('text.txt', 'r') as file:
#     # print(file.readline(8))
#     # print(file.readlines(14))
#     print(file.read(3))


# Hello world!
# My name is John Snow!
# I'm King of North!

# with open('text.txt', 'a') as file:
#     file.write('Pervaia Strocka!\n')
#     file.write('John Snow is bastard of Ned Stark!\n')
#     file.write('This is lesson about files!\n')
#     file.seek(0)
#     data = ['Bilal is genius!\n', 'Tima is good boy!\n']
#     file.writelines(data)

# with open('text.txt', 'r+') as file:
#     file.write('John Snow')
#     file.seek(0)
#     print(file.read())


# sudo apt update - обновление apt
# sudo apt install tesseract-oct - команда установки - вытаскивает из картинки инфо
# sudo apt install libtesseract-dev - команда установки - вытаскивает из картинки инфо

# pip install pytesseract
# pip install Pillow

# try:
#     from PIL import Image
# except ImportError:
#     import Image

# import pytesseract
# import re


# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string, type(string))
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n'for x in list_of_imei)

# image = 'imei.jpg'
# get_imei_code(image)

# with open('text.txt', 'w+') as file: 
#     file.write('0*1*2*3*4*5*6*7*8*9*')
#     file.seek(0)
#     data = file.read()
#     print(data)

# with open('text.txt', 'r') as file:
#     data = len(file.readlines())
#     print(data)


# with open('text.txt', 'r+') as file:
#     data = [int(x.replace(' \n', '')) for x in file.readlines()]
    
# with open('task6.txt', 'w+') as file:
#     file.write(f'{min(data)}-{max(data)}')


# def read_last(lines: int, filename: str):
#     with open(filename) as file:
#         list_ = file.readlines()
#         reversesed_list = list_[::-1]
#         if len(list_) > lines:
#             i = 0
#             while i < lines:
#                 print(reversesed_list[i].replace('\n', ''))
#                 i += 1
#         else:
#             for line in reversesed_list:
#                 print(line.replace('\n', ''))
           
# read_last(50, 'article.txt')

def longest_words(filename: str):
    with open(filename) as file:
        list_ = file.readlines()

    list_ = [x.replace('\n', '').strip() for x in list_]
    string = ''
    for item in list_:
        string = string + ' ' + item
    list_words = string.split()
    r = 0
    for i in range(len(list_words)):
        if r < len(list_words[i]):
                r = len(list_words[i])               
    longest_w = [list_words[i] for i in range(len(list_words)) if len(list_words[i]) == r]
    
    if len(longest_w) > 1:
         print(longest_w)
    else:
         print(longest_w[0])

longest_words('text.txt')
