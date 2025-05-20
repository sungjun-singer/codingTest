import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    val = 1

    graph[y][x] = 0
    stack = [(y, x)]

    while stack:
        cy, cx = stack.pop()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx]:
                    stack.append((ny, nx))
                    graph[ny][nx] = 0
                    val += 1
    return val

maxv = 0
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            cnt += 1
            maxv = max(dfs(i, j), maxv)

print(cnt)
print(maxv)