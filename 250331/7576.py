"""
1. 아이디어
    - 우선 1인 좌표를 전부 찾은다음에 큐에 넣는다 (y,x,cnt) 형식으로
    - 그리고 bfs를 돌리며 cnt+1을 해가며 ny, nx를 넣는다 (ny, nx, cnt + 1)로
    - 마지막에 큐가 비었을 때 현재 cnt를 리턴한다.
    - 토마토 배열을 다 뒤지고 0이 남아있다면 -1을 출력하고 아니라면 리턴한 cnt를 출력한다.
2. 시간복잡도
    - O(V+E) : 정점의 개수 : 100만 + 400만 -> 500만
3. 자료구조
    - 토마토 배열 : int [][]
    - 방문여부 배열 : bool [][]
"""

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))

dy = [0, 1, 0, -1]
dx = [1, 0 ,-1, 0]


maxv = 0
def bfs():
    global q
    global maxv
    while q:
        y, x, cnt = q.popleft()
        maxv = cnt
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx] == 0 and not visited[ny][nx]:
                    graph[ny][nx] = 1
                    visited[ny][nx] = True
                    q.append((ny,nx, cnt+1))

    return maxv

bfs()
flag = True

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = False
            break

if flag:
    print(maxv)
else:
    print(-1)




