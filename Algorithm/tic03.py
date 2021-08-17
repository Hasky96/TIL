N, M = map(int, input().split(' '))
data =[]
for i in range(N):
    data.append(list(map(int,input().split(' '))))

def getAns(N,data):
    choices = []
    for i in range(N):
        choices.append(min(data[i]))
    return max(choices)

print(getAns(N,data))
