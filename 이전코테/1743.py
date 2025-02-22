from collections import deque
import sys


input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
res = []

def bfs(y, x):
    q = deque([(y,x)])
    cnt = 1
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            res.append(bfs(i, j))

print(max(res))