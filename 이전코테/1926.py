"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1

여기서 그림의 갯수와 최대값을 출력하면 된다.
"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, graph):
    q = deque([(y, x)])
    cnt = 1
    visited[y][x] = True
    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1

    return cnt

max_value = 0
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            max_value = max(max_value, bfs(i,j, graph))
            count += 1


print(count)
print(max_value)

