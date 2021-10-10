# print(str(bin(19))[2:].index('1',4))

# a =[1, 2,5,67,23]
# print(a.index(67))
# a.remove(67)
# print(a)
# n=7
# lost= [2,3,4]
# reserve = [1,2,3,6]
# print(list(set(lost)-set(reserve)))
# def solution(n, lost, reserve):
#     # n : 전체 학생
#     lost.sort()
#     answer = n-len(lost)
#     for i in lost:
#         if i in reserve :
#             reserve.pop(reserve.index(i))
#             answer += 1
#         elif i-1 in reserve:
#             reserve.pop(reserve.index(i-1))
#             answer += 1
#         elif i+1 in reserve:
#             reserve.pop(reserve.index(i+1))
#             answer += 1
#     return answer

# print(solution(n, lost, reserve))
# a = 'adasd'
# print(len(a))
# print(set(a))
# for i in range(5):
#     print( i + 2)
# shorts = [1,2,3]
# def find(i=0):
#     if i == len(shorts):
#         print(shorts)
#     else:
#         for j in range(i+1, len(shorts)-1):
#             shorts[i],  shorts[j] = shorts[j],  shorts[i]
#             find(i+1)
#             shorts[i],  shorts[j] = shorts[j],  shorts[i]
#
#
# # find(0)
# arr = []
# arr.insert(0,9)
# print(arr)

# print('A'<'B')

# def comb(i,p,r):
#     if i == r:
#         print(arr[:r])
#     else:
#         for j in range(i, p):
#             arr[i], arr[j] = arr[j], arr[i]
#             comb(i+1, p, r)
#             arr[i], arr[j] = arr[j], arr[i]
#
#
# arr = [1, 2, 3, 4]
# comb(0, 4, 3)
# arr = [1,2,3,4]
# a= String(arr)
# class Q:
# #     def __init__(self, n):
# #         self.Q = [0] * n
# #         self.st = 0
# #         self.en = -1
# #
# #     def push(self, x):
# #         self.en += 1
# #         self.Q[self.en] = x
# #
# #     def pop(self):
# #         if self.st <= self.en:
# #             self.st += 1
# #             return self.Q[self.st-1]
# #         else:
# #             return -1
# #     def size(self):
# #         return self.en - self.st
# #
# #     def empty(self):
# #         return int(self.st > self.en)
# #
# #     def front(self):
# #         if self.st <= self.en :
# #             return self.Q[self.st]
# #         else:
# #             return -1
# #
# #     def back(self):
# #         if self.st <= self.en :
# #             return self.Q[self.en]
# #         else:
# #             return -1
# #
# # q=Q(3)
# # print(q.en)
# # q.push(3)
# # print(q.en)

from collections import deque
# str = [1,2,3,4,5,6]
# s = '123'
# print(list(s))
# print(str[0:4])
def find_next(n):
    # number list 0~9
    sn = str(n)
    len_n = len(sn)
    for idx in range(len(sn)-1):
        num_list = [0]*10
        num_list[int(sn[idx])] = 1
        for jdx in range(idx+1, len(sn)):
            int_sn = int(sn[jdx])
            if num_list[int(sn[jdx])]:
                if int_sn == 9:
                    sn = str(int(sn[:jdx+1])+1)
                    while len(sn) < len_n:
                        sn += '0'
                    print(n, 'function', sn)
                    return int(sn)
                sn = sn[:jdx]
                kdx = int_sn+1
                while True:
                    if not num_list[kdx]:
                        sn += str(kdx)
                        num_list[kdx] = 1
                    if len(sn) >= len_n:
                        return int(sn)
                    else:
                        kdx = -1
                    kdx += 1
print(find_next(1000))
# print('123'+'0'*3)