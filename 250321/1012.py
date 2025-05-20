"""
1. 아이디어
    - 필요한 배추 흰지렁이의 개수를 찾는 것이다.
    - 우선 그래프를 다 0으로 만들어두고 좌표의 배추를 1로 바꾼다.
    - 그리고 bfs 돌려서 bfs가 돌아간 횟수만 측정해서 출력한다.
2. 시간복잡도
    - BFS -> O(V+E) O(2500 + 4*2500) -> O(5*2500)
3. 자료구조
    - 밭을 표시하기 위한 이차원 배열 -> int [][]
    - 필요한 흰지렁이 개수를 출력하기 위한 변수 -> int
    - 테스트케이스, 가로, 세로, 배추 좌표 저장하기 위한 변수 -> int
"""

import sys
input = sys.stdin.readline


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    graph[y][x] = 0

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0 <= ny < n) and (0 <= nx < m):
            if graph[ny][nx] == 1:
                dfs(ny, nx)


T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)
