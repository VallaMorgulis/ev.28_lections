# num1 = 1

# while num1 >= 0:
#     num1 = input('Vvedite chislo: ')
#     if num1[0] == '-' and num1[1:].isdigit():
#         num1 = int(num1)
#     else:
#         num1 = 1

# print('Встретилось отрицательное число')

#-----------------------------------------

# from random import randint
# ls = []
# for x in range(0,100):
#     ls.append(randint(0, 100))
# ls.sort()
# print(ls, len(ls))

# li = []
# for i in ls:
#   if i not in li:
#     li.append(i)

# print(li, len(li))

# x1, y1, x2, y2 = int(input('Vvedite 1 coordinatu gde stoit ladya:')), int(input('Vvedite 1 coordinatu gde stoit ladya:')), int(input('Vvedite 1 coordinatu gde budet stoit ladya:')), int(input('Vvedite 1 coordinatu gde sbudet toit ladya:'))
# ladya = [x1, y1]
# tagret = [x2, y2]

# if x1 == x2 or y1 == y2:
#     print(True)
# else:
#     print(False)

# -------------------------------------------

# import random 

# ls = ['Plov', 'Besh-Barmak', 'Kuurdak', 'Oromo', 'Lagman']
# p = 0
# b = 0
# k = 0
# o = 0
# l = 0

# for x in range(0, 1_000_000):
#     meal = random.choice(ls)
# #    print(meal)
#     if meal.lower() == 'plov':
#         p += 1
#     elif meal.lower() == 'besh-barmak':
#         b += 1
#     elif meal.lower() == 'kuurdak':
#         k += 1
#     elif meal.lower() == 'oromo':
#         o += 1
#     else:
#         l += 1


# # print('Результаты голодных игр:')
# # print(f'Plov {p}\nBesh-Barmak {b}\nKuurdak {k}\nOromo {o}\nLagman {l}')

# dict_ = {'Plov': p, 'Besh_barmak': b, 'Kuurdak': k, 'Oromo': o, 'Lagman':l}
# print(dict_)
# res = sorted(dict_.items(), key=lambda x: x[1], reverse=True)[0]
# print(f'Gобедило блюдо {res[0]} и оно набрало: {res[1]} очков!')

# sorted_dict = {k:item for item in sorted(dict_.values(), reverse=True) for k,v in dict_.items() if item == v}
# print(sorted_dict)

###-----------------------------------

# random.choice(sequence) - случайный элемент непустой последовательности.



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# 1) nums = [2, 7. 11. 15]
# target = 9
# # 0, 1 ------------------------- 2 + 7 = 9

# 2) nums = [4, 11, 2, 5, 1, 6]
# target = 8
# 2,5 ----------------------------2 + 6 = 8

# nums = [4, 11, 2, 5, 1, 6]
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num != nums[i]:
#             print(f'Otvet: {i}, {nums.index(num)}')
#             break

# print(nums.index(5))    


# x, y, z = 102, 36, 90
# if x < z and x < y:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)

# x = 102
# y = 36
# z = 90
# if x < y and x< z: 
#     print(x) 
# elif y < x and y < z: 
#     print(y) 
# else: 
#     print(z)