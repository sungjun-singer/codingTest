"""
그림 문제 DFS로 풀기

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y,x):
    res = 1
    stack = [(y,x)]


    while stack:
        sy, sx = stack.pop()

        for k in range(4):
            ny = sy + dy[k]
            nx = sx + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((ny, nx))
                    res += 1
    return res


cnt = 0
maxv = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            maxv = max(dfs(i,j), maxv)

print(cnt)
print(maxv)




