x = int(input())
cnt = 0
while x != 1:
    if x >= 3 and x % 3 == 0:
        x = x // 3
        cnt += 1
    elif(x >= 3 and((x-1) % 3 ==0) and (((x-1)/3)%3==0)):
        x -=1
        cnt += 1
    elif(x >= 2 and x % 2 == 0):
        x = x // 2
        cnt += 1
    else:
        x -= 1
        cnt += 1
print(cnt)