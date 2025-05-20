"""
1. 아이디어
    - 상어의 크기는 2로 시작하고
    - 자기보다 큰 놈 앞은 못지나가고
    - 같으면 통과해서 지나갈 수 있고
    - 작은 놈은 먹을 수 있어
    - 먹을 수 있는 가장 가까운 물고기를 먹으러 간다.
    - 거리가 같다면 가장 위에 있는 물고기, 여러마리라면 왼쪽에 있는 물고기를 먹는다.
    - 상어의 크기와 같은 수만큼의 물고기를 먹어야지 크기가 1 커진다.
    -

2. 시간복잡도

3. 자료구조


"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
cnt = 0
y, x, size = 0,0,2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            y = i
            x = j

def bfs(y,x,shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    q = deque([(y,x)])

    visited[y][x] = 1
    tmp = []
    while q:
        cy, cx = q.popleft()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if (0<=ny<n) and (0<=nx<n) and visited[ny][nx] == 0:
                if graph[ny][nx] <= shark_size:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                    distance[ny][nx] = distance[cy][cx] + 1
                    if graph[ny][nx] < shark_size and graph[ny][nx] != 0:
                        tmp.append((ny, nx, distance[ny][nx]))

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
res = 0
while 1:
    shark = bfs(y, x, size)
    # 길이가 0이면 탐색 종료
    if len(shark) == 0:
        break

    ny, nx, dist = shark.pop()

    # 시간 더해주가
    res += dist
    graph[y][x], graph[ny][nx] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    y, x = ny, nx
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(res)