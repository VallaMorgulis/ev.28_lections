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


