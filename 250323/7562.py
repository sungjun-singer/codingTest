"""

1. 아이디어
    - 나이트의 현재 위치에서 지정된 위치까지 이동하게 되는 최소값을 구해야한다.
    - 최소값이니 BFS를 사용하면 될 것 같다.
    - 이동하는 방법은 8가지 (나이트가 이동하는 방법)
    - 시작 지점부터 해서 8가지 이동방향 큐에 넣어두고 방문하지 않은 지점만 이동가능하게
    - 그리고 큐에 넣을 때 depth가 몇인지 알아내야하는데
    - x-1, x+1, x*2 문제에서 했었는데, 그때는 이전 dist 배열을 만들어서 도달한 횟수를 출력하는 방식
    - 이것도 그냥 그렇게 하자 거리 저장하고 출력하는 방식으로
2. 시간복잡도
    - BFS -> O(V+E) -> 90000 + 4*90000 -=> 450000
    -
3. 자료구조
    - 체스판 거리 저장 배열 : int [][]
    - 방문 여부 : visited [][]
"""

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dy = [1,2,2,1,-1,-2,-2,-1]
dx = [2,1,-1,-2,-2,-1,1,2]

def bfs(y, x):
    q = deque([(y, x)])

    while q:
        qy, qx = q.popleft()

        if qy == goal_y and qx == goal_x:
            print(graph[qy][qx])
            return

        for k in range(8):
            ny = qy + dy[k]
            nx = qx + dx[k]

            if (0<=ny<n) and (0<=nx<n):
                if not graph[ny][nx]:
                    graph[ny][nx] = graph[qy][qx] + 1
                    q.append((ny,nx))

    print(graph[goal_y][goal_x])



for _ in range(T):
    n = int(input())

    cur_x, cur_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())

    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    bfs(cur_y, cur_x)




