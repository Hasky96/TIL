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
# find(0)
arr = []
arr.insert(0,9)
print(arr)