"""

1. 아이디어
    - 정사각형으로 이루어져 있는 섬과 바다 지도가 주어지는데
    - 이때 섬의 개수를 세는 프로그램을 작성
    - 땅은 1, 바다는 0
    - 섬을 찾으면 된다.
    - 최단경로 아니니 dfs가 더빠를 거다.
    - 0 0 이 들어오게 되면 테스트 케이스를 종료한다.
2. 시간복잡도
    - DFS(V+E) -> 2500 + 10000 -> 12500
    - 테스트 케이스의 개수는 안나와있어서 측정할수 없지만 복잡도가 초과되지는 않아보인다.
3. 자료구조
    - 지도 -> int [][]
    - 방문여부 -> visited [][]
    - 너비, 높이, 결과 -> int
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]

def dfs(y, x):
    visited[y][x] = True

    for k in range(8):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0<=ny<h) and (0<=nx<w):
            if graph[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)

while True:
    w, h = map(int, input().split())

    if h == 0 and w == 0:
        exit(0)

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    visited = [[False] * w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] and not visited[i][j]:
                cnt += 1
                dfs(i,j)

    print(cnt)