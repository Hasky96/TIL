
def sol(i,N):
    if i == N:
        print(a1)
    else:
        for j in range(i+1,N):
            a1[i], a1[j] = a1[j], a1[i]
            sol(i+1, N)
            a1[i], a1[j] = a1[j], a1[i]


a = input()
b = input()

a1 = []
a1.extend(a)
b1 = []
b1.extend(b)

sol(0, 3)


