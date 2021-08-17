N, M, K =  map(int,input().split(' '))
li = list(map(int,input().split(' ')))

def getValue(M, K, li):
    maxValue = max(li)
    li.pop(li.index(maxValue))
    newMax = max(li)
    if newMax==maxValue :
        return maxValue*M
    else:
        return maxValue*(M-M//K) + newMax*(M//K)

print(getValue(M, K, li))
