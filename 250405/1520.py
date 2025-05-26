"""
1. 아이디어
    - 0,0에서 시작해서 n-1,m-1 갈때까지 계속 현재 위치보다 작은 경로로 가야한다.
    - dfs를 돌면 되는거 같은데 DP랑 같이 간다.
    - 방문한거는 0으로 초기화 하며 가다가 마지막 좌표에 도달했을 경우, 현재 진행했던 경로에 다 +1 해준다.
    - 이후 -1이 아닌 다른 경로를 발견했을 때 이미 갔다와본 경로고 마지막 노드까지의 경로가 몇개있는지 저장되어 있기 때문에
    - 그 경로로 최신화하면서 진행한다.
2. 시간복잡도
    - O(V+E) -> 500*500 5*250000 -> 1250000
3. 자료구조
    - 지도 저장 그래프 : int [][]
    - 방문 여부 저장 그래프 : int [][]
"""

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

# 나는 세로가 n인게 더 편해서 n으로 진행 (문제에서는 m이 세로)
n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]



def dfs(y, x):
    # 마지막 좌표에 도달했을 경우
    if y == n-1 and x == m -1:
        return 1

    # 방문 처리
    if visited[y][x] == -1:
        visited[y][x] = 0

        dy = [0, 1, 0, -1]
        dx = [1, 0, -1, 0]

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                # 더 낮은 곳일 때 이동
                if graph[y][x] > graph[ny][nx]:
                    # 방문한 곳이 끝까지 가는 경로를 저장
                    visited[y][x] += dfs(ny, nx)

    return visited[y][x]

print(dfs(0, 0))