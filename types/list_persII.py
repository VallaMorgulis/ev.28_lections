# task 1

# name_of_friends = ['hello', 'world', 'python', 'makers', 'bootcamp']
# for i in name_of_friends:
#     print(i)

# task 2

# labels = ['Honda', 'Kawasaki', 'Mazda', 'Mersedess']
# for i in labels:
#     print(f'I like brand {i}')

# task 3

# name_of_list = ['tree']
# start = []
# end = []
# index = len(name_of_list[0]) / 2
# if index % 2 != 0:
#     index + 1
# for i in range(0, len(name_of_list[0])):
#     if i < index:
#         start.append(name_of_list[0][i])
#     else:
#         end.append(name_of_list[0][i])
# print(end + start)

# task 4

# list_ = ['world', 'hello', 'right']
# new_list = [x for x in list_[::-1]]
# print(new_list) 

# task 5

# goods = ['Coat1', 'Coat2', 'Coat3', 'Coat4', 'Coat5']
# suitcase = []
# for i in goods:
#     suitcase.append(i)

# suitcase.pop(-1)
# suitcase.insert(0, 'Pillow')
# print(suitcase)

# task 6

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = [x for x in nums if x < 5]
# print(res)

# task 7

# variable = input()
# list_ = variable.split(',')
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)

# task 8

# list_ = [1, 2, 3, 4, 5]
# new_list = [str(x) for x in list_]
# print(new_list)

# task 9

# list_ = [1, 2, 3, 4, 5]
# new_list = ['нечетное' if x % 2 != 0 else 'четное' for x in list_]
# print(new_list)

# task 10

# list_ = [x for x in range(20)]
# print(list_)

# task 11

# list_ = [x for x in range(101) if x % 2 == 0]
# print(list_)

# task 12

# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# print(sum(list1 + list2))

# task 13

# list_ = input().split(',')
# print(sorted(list_))

# task 14

# list_ = [1, 2, 3]
# mirror_set = set(list_)
# if len(list_) == len(mirror_set):
#     print('ERROR')
# else:
#     print('yes')

# task 15

# list_ = [x for x in range(54, 9184) if x % 5 == 0]
# print(list_)

# task 16

# list_ = [20, 10, 20, 1, 100]
# print(sorted(list_)[0])

# task 17

# 1

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = [x for x in tuples if x]
# print(cleared_tuples)

# 2

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# cleared_tuples = list(filter(None, tuples))
# print(cleared_tuples)

# task 18

# names = []
# for i in range(1,6):
#     name = input()
#     names.append(name.split()[-1])

# print(sorted(names))

# task 19

# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# print(list_.count(number))

# task 20

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# sum_ = 0
# for i in list_:
#     if type(i) == int:
#         sum_ += i
#     elif i.isdigit():
#         sum_ += int(i)

# print(sum_)

# task 21

# str_list = ['abc', 'xyz', 'aba', '1221']
# new_list = [index for index, value in enumerate(str_list) if value[0] == value[-1]]
# print(new_list)

# task 22

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]] 
# max_ = max([x for x in lists], key=len)
# print(max_)
# min_ = None 
# if len(lists) > 1: 
#     min_ = min([x for x in lists],key=len) 
# if max_ == min_: 
#     min_ = None 

# print(f'max_list {max_}') 
# print(f'min_list {min_}')


# МОЕ РЕШЕНИЕ

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_ = sorted(lists, key=len)[-1]
# min_ = sorted(lists, key=len)[0]
# if lists == [[]]:
#     print(f'max_list {[]}')
#     print(f'min_list {None}')
# elif max_ == min_:
#     print(f'max_list {max_}')
#     print(f'min_list {None}')
# else:
#     print(f'max_list {max_}')
#     print(f'min_list {min_}')




# task 23

# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = [list_[i::step] for i in range(len(list_))][:step] 
# print(new_list)

# task 24

# size = 3
# matrix = [[x for x in range(1, size+1)]]
# print(matrix * size)

# task 25

# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# user = input()
# proposal_word = [x for x in list_ if x.startswith(user)]
# print(proposal_word)

# task 26

# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# colors3 = set(colors1).difference(set(colors2))
# colors4 = set(colors2).difference(set(colors1))
# print(list(colors3), list(colors4))

# task 27



# https://leetcode.com/problems/add-two-numbers/
# def self():
# l1 = [2,4,3]
# l2 = [5,6,4]
# ch1 = [int(x) for x in str(int(''.join([str(x) for x in l1[::-1]])) + int(''.join([str(x) for x in l2[::-1]])))[::-1]]
# print(ch1)


# l1 = [0]
# l2 = [0]
# ch1 = int(''.join([str(x) for x in l1[::-1]]))
# ch2 = int(''.join([str(x) for x in l2[::-1]]))
# ch3 = ch1 + ch2
# ch_total = [int(x) for x in str(ch3)[::-1]]


# print(ch_total)



# def self(x):
#     y = [x for x in str(x)]
#     if y[0:] == y[::-1]:
#         return True
#     else:
#         return False
    
# print(self(121))


# https://leetcode.com/problems/plus-one/submissions/931868900/
# digits = [4,3,2,1]
# digits = list(str(int(''.join([str(x) for x in digits])) + 1))
# digits1 = [int(x) for x in digits]
# print(digits1, type(digits1))

# a = "1010"
# b = "1011"
# # print(hex(int(a)))
# res = bin(int(a)) + bin(int(b))
# print(res)



# https://leetcode.com/problems/two-sum/

# target = 6
# nums = [3, 4, 2, 12, 5, 6]

# def twoSum(nums, target):

#     ind_fin = []
#     nums_answer = [x for x in nums if (target - x) in nums]
#     if nums_answer[0] == nums_answer[1]:
#         ind = 0
#         for i in nums:
#             if i in nums_answer:
#                 ind_fin.append(ind)
#             ind += 1
#         return ind_fin
#     else:
#         nums_answer = [x for x in nums_answer.copy() if target / 2 != x]
#         ind = 0
#         for i in nums:
#             if i in nums_answer:
#                 ind_fin.append(ind)
#             ind += 1
#         return ind_fin

# print(twoSum(nums, target))


# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# s = 'bababcabcbb'
# res = 0
# sub = ''
# for char in s:
# 	if char not in sub:
# 		sub += char
# 		res = max(res, len(sub))
# 	else:
# 		cut = sub.index(char)
# 		sub = sub[cut+1:] + char

# print(res)

# https://leetcode.com/problems/single-number/

# nums = [4,4,1,2,1,2,3]
# check = []
# for i in nums:
#     if not i in check:
#         check.append(i)
#     elif i in check:
#         check.remove(i)

# print(check[0])


# https://leetcode.com/problems/median-of-two-sorted-arrays/

# nums1 = [1]
# nums2 = [1]

# def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:

#     nums3 = sorted(nums1 + nums2)

#     if not nums1 and not nums2:   
#         res = float(0)
#         return res
#     elif len(nums3) % 2 != 0:
#         i = len(nums3) // 2
#         res = float(nums3[i])
#         return res
#     else:
#         i = len(nums3) // 2
#         res = float((nums3[i] + nums3[i - 1]) / 2)
#         return res

# print(findMedianSortedArrays(nums1, nums2))


# https://leetcode.com/problems/merge-k-sorted-lists/   ---  Не проходит ответ на сайте, хотя работает

# lists = [[1],[1,3,4],[2,6]]
# list_ = []

# if lists == []:
#     print(list_)
# elif lists == [[]]:
#     print(lists[0])
# else:
#     for i in lists:
#         if i:
#             for x in range(0, len(i)):
#                 list_.append(i[x])

# list_ = sorted(list_)
# print(list_)
            


# https://leetcode.com/problems/length-of-last-word/  
# -  РЕШЕНО!!!!

# s = "  Hello World  "
# b = s.strip().split()
# len_ = len(b[-1])
# print(len_)

# https://leetcode.com/problems/remove-duplicates-from-sorted-list/ - Работает, но сайт не принимает.

# head = [1,1,2,3,3]
# sorted_ = []
# for i in head:
#     if not i in sorted_:
#         sorted_.append(i)

# print(sorted_)

# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ] 

# def func21(products, category):
#     res = [x for x in products if x['category'].lower() == category.lower()]
#     return res

# print(func21(products, 'apple'))





