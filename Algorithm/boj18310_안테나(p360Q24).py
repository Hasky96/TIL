
N = int(input())

homes = list(map(int, input().split()))
homes.sort()
left, right = 0, 0

first = homes[0]
last = homes[-1]
i = 0
j = N-1
while i != homes:
    i += 1
    left += homes[i] - first
    if i == j :
        break
    j -= 1
    right += last - homes[j]
print(left, right)