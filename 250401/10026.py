"""
1. 아이디어
    - 빨간색이랑 초록색의 차이를 거의 못 느낀다.
    - 배열 다 돈다음에 빨간색을 초록색으로 바꾼다.
    - 그리고 DFS 돈다.
2. 시간복잡도
    - O(V+E) -> 100 * 100
3. 자료구조


"""

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global init
    stack = [(y,x)]
    visited[y][x] = True

    while stack:
        cy, cx = stack.pop()

        for k in range(4):
            ny = cy + dy[k]
            nx = cx + dx[k]

            if (0<=ny<n) and (0<=nx<n):
                if not visited[ny][nx] and graph[ny][nx] == init:
                    stack.append((ny, nx))
                    visited[ny][nx] = True

init = ''
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            init = graph[i][j]
            dfs(i, j)

print(cnt, end=' ')

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

init = ''
cnt = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            init = graph[i][j]
            dfs(i, j)

print(cnt)