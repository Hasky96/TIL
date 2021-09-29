def comparator(o):
    return o[1] + float('0.'+str(o[0])[::-1])


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr.sort(key=comparator, reverse=True)
# print(arr)
cnt = 0
end = 0
while arr:
    meeting = arr.pop()
    if meeting[0] >= end:
        cnt += 1
        end = meeting[1]
print(cnt)