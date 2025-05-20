# """
# 1. 아이디어
#     - 왼쪽 위에서 오른쪽 아래로 점프하여 이동
#     - 점프는 오른쪽 혹은 아래쪽으로만 해야한다.
#     - 0은 진행을 못하게 하는 종착점이다.
#     - 오른쪽, 아래만 해서 dfs 돌리는데 방문 여부는 딱히 저장할 필요가 없다.
#     - 배열 밖을 벗어나면 끝이고, 마지막 0이 나온다면 +1
#     - 끝
# 2. 시간복잡도
#     - 게임판의 크기 100
#     - dfs -> O(V+E) 10000 + 4*10000 -> 50000
# 3. 자료구조
#     - 게임판 저장 배열 : int [][]
#     -
# """
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# dy = [0, 1]
# dx = [1, 0]
#
# visited = [[False] * n for _ in range(n)]
#
# res = 0
#
# def dfs(y, x):
#     global res
#     if graph[y][x] == 0:
#         res += 1
#         return
#
#     visited[y][x] = True
#
#     for k in range(2):
#         ny = y + (dy[k]*graph[y][x])
#         nx = x + (dx[k]*graph[y][x])
#
#         if (0<=ny<n) and (0<=nx<n):
#             dfs(ny, nx)
#
#     visited[y][x] = False
#
# dfs(0,0)
# print(res)

"""
dfs는 방문여부를 체크해서
이미 방문한걸 또 방문하지 못하게 처리하는 것이 불가능해서
시간 초과가 난다.
시간 초과가 나와 DP로 풀어본다.

1. 아이디어
    - dp 배열을 만든다.
    - 0,0부터 시작해서 도달 하는 경로의 수를 더해준다.
    - 마지막 0에 도달하는 경로의 수를 출력한다.
2. 시간복잡도
    - O(n^2) -> 10,000
3. 자료구조
    - 게임판 : int [100][100]
    - dp배열 : int [100][100]
"""

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]


dp[0][0] = 1
for i in range(n):
    for j in range(n):
        k = graph[i][j]

        if k == 0 or dp[i][j] == 0:
            continue
        if i+k < n:
            dp[i+k][j] += dp[i][j]
        if j+k < n:
            dp[i][j+k] += dp[i][j]

print(dp[n-1][n-1])

