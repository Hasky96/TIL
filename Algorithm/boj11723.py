M = int(input())

li=[]
for i in range(M):
    inp=input()
    if ' ' in inp:
        m,a = inp.split()
        a = int(a)
    else:
        if m == 'all':
            li = list(range(1, 21))

        elif m == 'empty':
            li = []
    
    if m == 'add':
        if a not in li:
            li.append(a)

    elif m == 'remove':
        if a in li:
            li.remove(a)

    elif m == 'check':
        if a in li:
            print('1')
        else:
            print('0')

    elif m == 'toggle':
        if a in li:
            li.remove(a)
        else:
            li.append(a)





