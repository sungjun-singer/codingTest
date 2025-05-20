"""
1. 아이디어
    - 떨어져있는 단지를 구하고 갯수를 구하는 문제
    - 최단거리를 구할 필요가 없으니 dfs가 좀더 효율적인 알고리즘
2. 시간복잡도
    - dfs O(V+E) 5*25*25 -> 3125
3. 자료구조
    - 단지 배열 -> int [][]
    - 방문 여부 -> bool [][]
    - 단지의 아파트 수 저장 배열 -> int []
"""

import sys
input = sys.stdin.readline

n = int(input())


graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global count

    visited[y][x] = True
    count += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0<=ny<n) and (0<=nx<n):
            if graph[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)


res = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            count = 0
            dfs(i, j)
            res.append(count)

res.sort()
print(len(res))

for x in res:
    print(x)