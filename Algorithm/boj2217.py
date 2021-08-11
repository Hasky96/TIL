# 로프

# 로프의 수
ropes = int(input())

rope_list =[]
for rope in range(ropes):
    rope_list.append(int(input()))

rope_list.sort()
weight = []
while len(rope_list)>0:
    weight.append(rope_list.pop(0) * (len(rope_list)+1))

print(max(weight))