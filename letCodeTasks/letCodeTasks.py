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

