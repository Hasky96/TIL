# dfs
def dfs(x, y):
    global union
    pass


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, L, R = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
while True:
    unions = []
    if len(unions) == N**2:
        break
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = [(i, j)]
                visited[i, j] = 1
                dfs(i, j)
                unions.append(union)
    print(unions)
    cnt += 1

