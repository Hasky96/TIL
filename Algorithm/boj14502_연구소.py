# 연구소
# BFS 전부 확인해보자
# 3 <= N, M <= 8
# 0 : space, 1 : wall, 3 : virus

import sys
input = sys.stdin.readline

N, M = tuple(map(int, input().split()))
lab = []

for _ in range(N):
    arr = []
    arr.extend(list(map(int, input().split())))
    lab.append(arr)

# 2차원 배열에 3개의 벽을 놓는 경우의 수
lab_arr = []
for i in range(N):
    lab_arr.extend(lab[i])

for a in range(N*M-2):
    lab_arr[a] = 1
    for b in range(a, N*M-1):
        lab_arr[b] = 1
        for c in range(b, N*M):
            lab_arr[c] = 1
            find(lab_arr)