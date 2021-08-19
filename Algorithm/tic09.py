
def solution(s):
    answer = 0

    length = [''] * (len(s) + 1)

    # 패턴길이 for
    for i in range(1, len(s)+1):
        idx = 0
        pattern = s[idx:idx+i]
        # pattern 비교 for
        cnt = 0
        for j in range(0, len(s)):
            # print(s[j], end=' ')
            if pattern == s[j]:
                cnt += 1
            if pattern != s[j] or j + 1 == len(s):
                length[i] += pattern
                pattern = s[j:j+i]
                print(pattern)
                if cnt > 1:
                    length[i] += str(cnt)
                cnt = 1

            idx += i
        print()

    print(length)
    return answer

s='aabbaccc'
print(solution(s))
