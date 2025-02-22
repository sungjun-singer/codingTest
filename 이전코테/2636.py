import sys
from collections import deque

input = sys.stdin.readline
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
changed = [[False] * m for _ in range(n)]
is_outside = [[False] * m for _ in range(n)]
is_expose = [[0] * m for _ in range(n)]


def is_out(graph):
    q = deque([(0, 0)])
    is_outside[0][0] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if graph[ny][nx] == 0 and not is_outside[ny][nx]:
                is_outside[ny][nx] = True
                q.append((ny,nx))

def arr_sum(graph):
    result = 0
    for x in graph:
        result += sum(x)

    return result

def is_end(graph):
    for x in graph:
        if sum(x) != 0:
            return True
    return False


def bfs(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if graph[ny][nx] == 0 and not changed[ny][nx] and is_outside[ny][nx]:
            is_expose[y][x] += 1

    if is_expose[y][x] >= 2:
        graph[y][x] = 0
        changed[y][x] = True
        return

is_out(graph)

cnt = 0

while is_end(graph):
    changed = [[False] * m for _ in range(n)]
    is_outside = [[False] * m for _ in range(n)]
    is_expose = [[0] * m for _ in range(n)]
    is_out(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
    cnt += 1

print(cnt)