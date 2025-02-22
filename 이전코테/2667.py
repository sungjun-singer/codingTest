# from collections import deque
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# res = []
#
# graph = []
# for _ in range(n):
#     arr = list(map(int, input().rstrip()))
#     graph.append(arr)
#
# visited = [[False] * n for _ in range(n)]
#
#
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]
#
# def bfs(y, x, graph):
#     cnt = 1
#     q = deque([(y,x)])
#
#     while q:
#         y, x = q.popleft()
#
#         visited[y][x] = True
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#
#             if 0 <= ny < n and 0 <= nx < n:
#                 if graph[ny][nx] and not visited[ny][nx]:
#                     visited[ny][nx] = True
#                     q.append((ny, nx))
#                     cnt += 1
#
#     return cnt
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] and not visited[i][j]:
#             res.append(bfs(i,j, graph))
# res.sort()
#
# print(len(res))
# for x in res:
#     print(x)




"""
이번엔 DFS로 구현해보자
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y,x):
    global each
    each += 1
    visited[y][x] = True

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)


each = 0
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            each = 0
            dfs(i, j)
            res.append(each)

res.sort()
print(len(res))
for x in res:
    print(x)