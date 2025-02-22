from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            cnt += 1

print(cnt)