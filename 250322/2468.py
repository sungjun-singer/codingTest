"""
1. 아이디어
    - 건물의 최대 높이를 구하고 그 높이만큼 반복문을 돌린다.
    - 비 높이보다 건물 높이가 높을 경우, 방문하지 않았을 경우 수행한다.
    - 최소거리가 아니니 dfs로 수행하는 것이 시간복잡도가 높을 것이다.
    -
2. 시간복잡도
    - 높이 * DFS(V + E) 100 * DFS(10000 + 40000) -> 5,000,000
    - 최대 높이 찾기 n^2
3. 자료구조
    - 건물 높이 배열 -> int [][]
    - 방문여부 배열 -> bool [][]
    - 안전영역 배열 -> int []
    - 배열의 길이, 높이, 최대높이, 수행횟수 -> int
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

maxv = 0
for x in graph:
    maxv = max(max(x), maxv)

dy = [0, 1, 0, -1]
dx = [1, 0 , -1, 0]

def dfs(y, x, h):
    visited[y][x] = True

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0<=ny<n) and (0<=nx<n):
            if graph[ny][nx] > h and not visited[ny][nx]:
                dfs(ny, nx, h)

res = 0

for h in range(maxv+1):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and not visited[i][j]:
                cnt += 1
                dfs(i,j,h)
    res = max(cnt, res)

print(res)