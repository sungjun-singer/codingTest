import sys
input = sys.stdin.readline

dy = [0,1,1,1,0,-1,-1,-1]
dx = [1,1,0,-1,-1,-1,0,1]

def dfs(y, x):

    if graph[y][x] == 0:
        return

    graph[y][x] = 0

    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < b and 0 <= nx < a:
            if graph[ny][nx] != 0:
                dfs(ny, nx)

res = []

while 1:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(b)]
    cnt = 0
    for i in range(b):
        for j in range(a):
            if graph[i][j] == 1:
                cnt +=1
                dfs(i, j)

    res.append(cnt)


for i in range(len(res) - 1):
    print(res[i])

print(res[len(res) - 1], end="")