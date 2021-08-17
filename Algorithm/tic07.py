#BOJ18406

N = input()

def solution(N):
    lucky = 0
    for i in range(len(N)//2):
        lucky += int(N[i])-int(N[-i-1])
    if lucky == 0:
        print('LUCKY')
    else:
        print('READY')

solution(N)