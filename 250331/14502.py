"""
1. 아이디어
    - 잘 모르겠지만 백트래킹과 bfs를 사용해서 푼다고 한다.
2. 시간복잡도
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
3. 자료구조

"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y,x):
    tmp_graph = graph
    q = deque((y,x))

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                if tmp_graph[ny][nx] == 0:
                    tmp_graph[ny][nx] = 2
                    q.append((ny,nx))



def makewall(cnt):
    if cnt == 3:
        bfs()
        return

