# first_dict = {
#     'first': 1, 
#     (1, 2, 3): ['wer', True, 1],
#     1.5: 'qwerty',
#     }
# for k in first_dict:
#     print(first_dict[k])

#-------------------------------------

# catalog = {}
# for i in range(3):
#     title = input('Введите наименование: ')
#     amount = input('Введите количество: ')
#     catalog[title] = amount

# for k,v in catalog.items():
#     print(f'{k}: {v}')

#--------------------------------------

# catalog = {}
# for i in range(3):
#     title = input('Введите наименование: ')
#     amount = int(input('Введите количество: '))
#     if title in catalog:
#         past = catalog[title]
#         catalog[title] = amount + past
#     else:
#         catalog[title] = amount

# for k,v in catalog.items():
#     print(f'{k}: {v}')

#----------------------------------

# string = input().lower()
# list_ = string.replace('.', ' ').replace(',', ' ').split()
# dict_= {}
# for i in range(len(list_)):
#     for word in list_:
#         dict_[word] = list_.count(word)

# for k,v in dict_.items():
#     print(f'{k}: {v}')

#------------------------------------------

# string = input().lower()
# list_ = string.replace('.', ' ').replace(',', ' ').split()
# dict_= {}
# for i in range(len(list_)):
#     for word in list_:
#         dict_[word] = list_.count(word)

# sorted_dict = dict(sorted(dict_.items(), key=lambda x: x[0]))

# for k,v in sorted_dict.items():
#     print(f'{k}: {v}')       
               



