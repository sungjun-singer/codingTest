"""
1. 아이디어
     - 0은 이동하는 곳 1은 이동할 수 없는 벽
     - 1,1 에서 N, M 으로 이동하는 최단 경로
     - 근데 벽을 하나정도 부셔도 좋다. -> 백트래킹
     - 모든 벽 하나씩 부셔보고 bfs 돌아서 최단경로
     - 만약에 1,2나 2,1 둘다 벽이라면 두개 벽만 한번씩 허물어보면 되고
     - 돌아가는 구간을 어떻게 알아차리지?
2. 시간복잡도
    - 이렇게 했을 때 시간복잡도는
    - bfs O(V+E) -> 5* 1000 * 1000 500만인데 4번 돌면 2000만이라 시간복잡도 안될 듯 한데
3. 자료구조

"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

# visited 배열 (상태 구분(0,1) 하고 전부 0으로 초기화)
visited = [[[0] * m for _ in range(n)] for _ in range(2)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(break_cnt, y, x):
    q = deque([(break_cnt, y, x)])

    # 초기 값 방문 처리 및 거리 저장
    visited[0][y][x] = 1

    while q:
        break_cnt, y, x = q.popleft()

        # 만약 마지막 좌표에 도달했다면 그 값 반환
        if y == n-1 and x == m-1:
            return visited[break_cnt][y][x]


        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                # 다음 이동하는 곳이 길이고 한번도 방문하지 않은 곳일 때
                if graph[ny][nx] == 0 and visited[break_cnt][ny][nx] == 0:
                    # 현재 상태(0 or 1)에 이전 좌표 거리 + 1 해서 방문처리 및 거리 저장
                    visited[break_cnt][ny][nx] = visited[break_cnt][y][x] + 1
                    q.append((break_cnt, ny, nx))

                # 다음이동하는 곳이 벽인데 벽 깰 기회가 남은 경우
                if graph[ny][nx] == 1 and break_cnt == 0:
                    # 벽을 부수고 상태값 1로 설정하고 안 깼던 이전 좌표의 거리 + 1 해서 저장
                    visited[1][ny][nx] = visited[0][y][x] + 1
                    q.append((1, ny, nx))

    # 마지막에 도달하지 못하고 벽에 막혔을 경우 -1 리턴
    return -1

print(bfs(0,0,0))








