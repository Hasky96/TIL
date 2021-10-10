def find_next(n):
    num_list = [0]*10
    len_n = len(str(n))
    return 1


ans_list = []

num = 1
while len(ans_list) <= 10000:
    # 겹치는 숫자가 있다면
    if 2 <= len(str(num)) != len(set(str(num))):
        num = find_next(num)
        print(num)
    else:
        ans_list.append(num)
        print(num)
        # 숫자 증가
        num += 1
print(ans_list[9999])
