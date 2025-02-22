"""
8 9 10

1 2 8 9 10
"""

from collections import deque

a,b,c = map(int, input().split())

q = deque([(0, 0)])

visited = [[False] * (b+1) for _ in range(a + 1)]
visited[0][0] = True

answer = []

def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

def bfs():
    while q:
        # A물통에 있는 물 : x, B물통에 있는 물 : y, C물통에 있는 물 : z
        x, y = q.popleft()
        z = c - x - y

        # A 물통이 비어있는 경우에 C 물통에 남아있는 양 저장
        if x == 0:
            answer.append(z)

        # A에서 B로 물 이동
        water = min(x, b- y)
        pour(x - water, y + water)
