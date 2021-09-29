import sys

input = sys.stdin.readline


def next_num(n):
    global num
    n = str(n)
    l = len(n)
    if l == len(set(n)):
        num = int(n)
        return
    else:
        for i in range(l - 1):
            for j in range(i + 1, l):
                if n[i] == n[j]:
                    n = (int(n[:j + 1]) + 1) * 10 ** (l - 1 - j)
                    return next_num(n)


ans = [0] * 1000001
num = 0
cnt = 0
while not ans[1000000]:
    cnt += 1
    next_num(ans[cnt-1]+1)
    ans[cnt] = num

while True:
    inp = int(input())
    if not inp:
        break
    print(ans[inp])


