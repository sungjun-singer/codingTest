"""
이론 정리

그래프 탐색
- BFS : 너비 우선 탐색 / 시간복잡도 O(Vertex+Edge)
- DFS : 깊이 우선 탐색

1. 아이디어
    - 일단 배열을 전부다 돌며 1을 찾고 visited로 방문처리하고
    - 근데 그냥 방문처리 안하고 0으로 만들어 버린다면 visited를 작성할 필요가 없겠지
    - 그냥 그래프만 가지고 해보자

2. 시간복잡도
    - BFS -> O(V+E) 500*500 + 4*500*500 -> 5*25000 -> 125000

3. 자료구조
    - graph : int[][]
    - res : int[]

"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
res = []

def bfs(y, x):
    res = 1
    q = deque([(y,x)])
    visited[y][x] = True

    while q:
        qy, qx = q.popleft()
        for k in range(4):
            ny = qy + dy[k]
            nx = qx + dx[k]

            if (0 <= ny < n) and (0<=nx<m):
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    res += 1
                    q.append((ny,nx))

    return res

maxv = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            maxv = max(bfs(i,j), maxv)

print(cnt)
print(maxv)