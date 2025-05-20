"""
1. 아이디어
    - 그냥 bfs 돌면서 연결된 1의 개수 세고 배열에 push하고
    - 배열의 개수 출력, 오름차순 정렬해서 요소 하나씩 출력하면 끝일듯
2. 시간복잡도
    - BFS -> O(V + E) -> O(25*25 + 4*25*25) -> O(5*25*25) 가능
3. 자료구조
    - 그래프 저장할 배열 -> int [][]
    - 방문 여부 저장할 배열 -> bool [][]
    - 결과 저장할 배열 -> int []
    - N
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[False] * n for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    cnt = 1
    q = deque([(y,x)])
    # 첫번째 방문 처리
    visited[y][x] = True

    while q:
        qy, qx = q.popleft()

        for k in range(4):
            ny = qy + dy[k]
            nx = qx + dx[k]

            if (0<=ny<n) and (0<=nx<n):
                if graph[ny][nx] and not visited[ny][nx]:
                    # 큐에 넣을 때 방문 처리
                    visited[ny][nx] = True
                    cnt += 1
                    q.append((ny, nx))
    return cnt

res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            res.append(bfs(i, j))

res.sort()

print(len(res))
for x in res:
    print(x)