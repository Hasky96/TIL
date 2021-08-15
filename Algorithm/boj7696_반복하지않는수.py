# 반복하지 않는 수

while True:
    n = int(input())
    if n == 0:
        break
    arr = [0] * 1000001

    for i in range(1, n+1):
        value = arr[i-1] + 1
        idx = len(str(value))
        while True:
            jfor = 1
            for j in range(idx-1):
                for k in range(j+1,idx):
                    if value//10**(idx-1-j) == value//10**(idx-1-k):
                        value //= 10**(idx-1-k)
                        value += 1
                        value *= 10**(idx-1-k)
                        jfor = 0 
                        break;
                if jfor == 0:
                    break
            if jfor == 1 :
                break
        arr[i] = value
    print(arr[n])

