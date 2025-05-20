"""
1. 아이디어
    - 3차원 배열로 토마토를 저장한 다음에 1을 다 찾고 큐에 넣는다.
    - bfs를 돌면서 이전 값에 +1 하면서 진행한다.
    - 마지막 bfs에 1보다 작은 값이 있다면 -1을 출력하고 끝내고
    - 아니라면 가장 큰 값을 계속 갱신하며 진행한다.
2. 시간복잡도
    - 전체 배열 돌면서 1 찾는 과정 100만
    - bfs는 O(V+E)
    - 정점의 개수 : 100 * 100 * 100 -> 100만
    - 간선의 개수 : 4 * 100만 -> 400만
    - bfs 돈 이후 전체 배열 돌면서 출력값 찾기 -> 100만
    - 100만 + 100만 + 400만 + 100만 -> 700만
3. 자료구조
    - 3차원 배열 : int [][][]
"""

import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

q = deque()


dz = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 0, 1, 0, -1]
dx = [0, 0, 1, 0, -1, 0]

def bfs():
    while q:
        cz, cy, cx = q.popleft()

        for k in range(6):
            nz = cz + dz[k]
            ny = cy + dy[k]
            nx = cx + dx[k]

            if (0<=nz<h) and (0<=ny<n) and (0<=nx<m):
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[cz][cy][cx] + 1
                    q.append((nz, ny, nx))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                q.append((i, j, k))

bfs()
max_value = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                exit(0)
            max_value = max(max_value, graph[i][j][k])

print(max_value-1)



