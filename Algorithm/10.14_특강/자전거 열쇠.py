# 비밀번호 4자리
N = 4
pw = [ [] for _ in range(N)]
def solution(level):
    global pw

    if level == 4:
        print(pw)
        return

    for i in range(9):
        if level == 0 and not (i == 6 or i == 8):
            continue
        pw[level] = i + 1
        solution(level + 1)



solution(0)


