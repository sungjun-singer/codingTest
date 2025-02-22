"""
4 6
101111
101010
101011
111011
"""

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(graph):
    q = deque([(0,0)])
    visited[0][0] = True

    while q:
        y, x = q.popleft()
        if y == n -1 and x == m - 1:
            return graph[n-1][m-1]

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1

    return graph[n-1][m-1]

print(bfs(graph))