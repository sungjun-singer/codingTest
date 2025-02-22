from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def common_bfs(y,x, graph):
    start = graph[y][x]

    q = deque([(y,x)])
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0<= nx < n:
                if graph[ny][nx] == start and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))

def handi_bfs(y, x, graph):
    start = graph[y][x]
    is_blue = False

    if start == 'B':
        is_blue = True

    q = deque([(y,x)])
    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < n:
                if not visited[ny][nx]:
                   if is_blue:
                       if graph[ny][nx] == "B":
                            visited[ny][nx] = True
                            q.append((ny, nx))
                   else:
                       if graph[ny][nx] != "B":
                            visited[ny][nx] = True
                            q.append((ny,nx))

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            common_bfs(i, j, graph)
            cnt += 1

print(cnt, end=' ')
visited = [[False] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            handi_bfs(i,j, graph)
            cnt += 1

print(cnt)