
M = int(input())

# empty list
S = []

for _ in range(M):

    # 연산과 수 받아오기
    process = input()
    if 'add' in process:
        num = int(process.split()[1])
        if num not in S:
            S.append(num)
    
    elif 'check' in process:
        num = int(process.split()[1])
        if num in S:
            print(1)
        else:
            print(0)
    
    elif 'remove' in process:
        num = int(process.split()[1])
        if num in S:
            S.remove(num)

    elif 'toggle' in process:
        num = int(process.split()[1])
        if num in S:
            S.remove(num)
        else:
            S.append(num)

    elif 'all' in process:
        S = list(range(1,21))

    elif 'empty' in process:
        S = []



