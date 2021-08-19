import sys

sys.stdin = open('tic13.txt')


def distance(adr1, adr2):
    return abs(adr1[0] - adr2[0]) + abs(adr1[1] - adr2[1])


N, M = tuple(map(int, input().split()))

arr_map = [list(map(int, input().split())) for _ in range(N)]
bhc = []
home = []

for i in range(N):
    for j in range(N):
        if arr_map[i][j] == 1:
            home.append((i, j))
        elif arr_map[i][j] == 2:
            bhc.append((i, j))

arr_dis = []

for c_adr in bhc:
    b_h = []
    for h_adr in home:
        b_h.append(distance(c_adr, h_adr))
    arr_dis.append(b_h)

print(arr_dis)
