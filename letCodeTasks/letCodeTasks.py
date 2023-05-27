# 48. Rotate Image

# class Solution:
#     def rotate(self, M: list[list[int]]) -> None:
#         n = len(M)
#         depth = n // 2
#         for i in range(depth):
#             rlen, opp = n - 2 * i - 1, n - 1 - i
#             for j in range(rlen):
#                 temp = M[i][i+j]
#                 M[i][i+j] = M[opp-j][i]
#                 M[opp-j][i] = M[opp][opp-j]
#                 M[opp][opp-j] = M[i+j][opp]
#                 M[i+j][opp] = temp


'''Другой вариант решения'''
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix[:] = [list(r) for r in zip(*reversed(matrix))]  
# print(matrix[:])


# class A:

#     def change(self):
#         print('Hello')

# class B(A):

#     def change(self):
#         # A.change(self)
#         super().change()

# obj = B()
# obj.change()


# class A:
#     def hello(self):
#         print('hello world')

# class B:
#     def hello(self):
#         print('HELLO WORLD')

# class C(A, B):
#     pass

# obj = C()
# obj.hello()

# class A:

#     @staticmethod
#     def change():
#         print('Hello')

# # class B(A):

# #     def change(self):
# #         # A.change(self)
# #         super().change()

# obj = A()
# obj.change()


class Students:

    @classmethod
    def do_homework(cls):
        print('I am doing my homework')

    def get_grade(self, grade):
        print(f'I got {grade} for my homework')

    @staticmethod
    def sleep():
        print('Zzzz')

student = Students()
student.do_homework()
Students.sleep()
Students.get_grade(student, 'B+')
# Students.get_grade('A+')