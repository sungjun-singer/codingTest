"""
1. 아이디어
    - x-1, x+1, x*2를 nx로 두고 bfs 진행한다.
    - 처음엔 4, 6, 10이 되고
    - 그 이후엔 (3,5,8), (5,7,12), (9,11,20)이 된다.
2. 시간복잡도
    - BFS -> O(V+E) -> O(100000 + 3*100000) -> 400000

3. 자료구조
    - 거리별로 걸리는 시간을 저장한 배열 -> int []
    - 첫시작점 n, 끝점 k -> int
    - bfs돌리기 위한 큐 -> deque
    - 큐에서 꺼낸 요소 저장 변수 -> int
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

dist = [0] * 100001

def bfs():
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            print(dist[k])
            break

        for nx in (x-1, x+1, x*2):
            if (0<=nx<100001) and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()