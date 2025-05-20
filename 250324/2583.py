"""

1. 아이디어
    - 모눈종이가 있는데 여기에 직사각형을 그린다.
    - 직사각형이 안그려진 부분의 영역 크기를 출력한다.
    - 아래 좌표에 있는 부분의 1을 0으로 바꿔준다.
    - 그리고 dfs를 돌리고 오름차순 정렬해서 출력한다.
2. 시간복잡도
    - DFS -> O(V+E) -> 10000 + 40000 -> 50000
3. 자료구조
    - 모눈 종이 : int [][]
    - 방문 여부 : bool [][]
    - 입력변수들 : int
    - 출력 배열 : int []
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [[1] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 <= x2:
        a = x1
        b = x2
    else:
        a = x2
        b = x1

    if y1 <= y2:
        c = y1
        d = y2
    else:
        c = y2
        d = y1

    for i in range(a, b):
        for j in range(c, d):
            graph[j][i] = 0


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global cnt

    graph[y][x] = 0

    cnt += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0<=ny<n) and (0<=nx<m):
            if graph[ny][nx]:
                dfs(ny, nx)

cnt = 0
res = []

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            cnt = 0
            dfs(i, j)
            res.append(cnt)
res.sort()

print(len(res))
print(" ".join(map(str, res)))



