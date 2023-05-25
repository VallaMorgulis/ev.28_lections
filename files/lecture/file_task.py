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

# def longest_words(filename: str):
#     with open(filename) as file:
#         list_ = file.readlines()

#     list_ = [x.replace('\n', '').strip() for x in list_]
#     string = ''
#     for item in list_:
#         string = string + ' ' + item
#     list_words = string.split()
#     r = 0
#     for i in range(len(list_words)):
#         if r < len(list_words[i]):
#                 r = len(list_words[i])               
#     longest_w = [list_words[i] for i in range(len(list_words)) if len(list_words[i]) == r]
    
#     if len(longest_w) > 1:
#          print(longest_w)
#     else:
#          print(longest_w[0])

# longest_words('text.txt')

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Пока там не работает - здесь работает

# nums = [1,1,2]
# new_nums = []
# k = 0
# for i in nums:
#     if not i in new_nums:
#         new_nums.insert(k, i)
#         k += 1
#     else:
#         new_nums.append('_')

# print(k, new_nums)

# task 9



# def calc_price(filename: str) -> int:
#     with open(filename, 'r') as file:
#         data = [x.replace('\n', '').split('   ') for x in file.readlines()]
#         res = sum([int(listik[1])*int(listik[2]) for listik in data])
    
#     return res

# filename = 'prices.txt'
# print(calc_price(filename))

# task 10

# import csv
# def read_csv(filename: str) -> dict[str, list[str]]:
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         result = {}
#         for row in reader:
#             key = row[0] 
#             values = row[1:] 
#             result[key] = values 
        
#         return result 

# result = read_csv('data.csv') 
# print(result)

# task 11

# def filter_text(text_filename: str) -> str: 
#     with open(text_filename) as f: 
#         word = (f.read()) 
#         word1 = word.lower()
        
#     with open('forbidden_words.txt') as f: 
#         forbidden = f.readline().split()
#         for i in forbidden: 
#             word1 = word1.replace(i, '*' * len(i))
#             list_1 = list(word1) 
#             list_ = list(word) 
#             for i in range(0, len(word1)): 
#                 print(list_1[i])
#                 print(list_[i].swapcase())
#                 if list_1[i] == list_[i].swapcase(): 
#                     list_1[i] = list_[i] 
#             a = ''.join(list_1) 
#     return a 

# filter_text('bad_text.txt')

# task 12

# def bad_students(filename: str) -> list[str]:
#     with open(filename) as file:
#         list_ = file.readlines()
#         list_last_names = []
#         for item in list_:
#             list_i = item.split()
#             if int(list_i[2]) < 4:
#                 list_last_names.append(list_i[1])

#     return list_last_names

# filename = 'students.txt'
# print(bad_students(filename))

# task 13

# def reverse_file_print(filename: str) -> None:
#     with open(filename) as file:
#         list_ = file.readlines()
#         list_ = [x[::-1] for x in list_]
#         list_rev = '\n'.join(list_)
#     print(list_rev)

# filename = 'zen_of_python.txt'
# reverse_file_print(filename)


import json
json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])


