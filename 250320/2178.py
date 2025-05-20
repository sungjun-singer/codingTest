"""
1. 아이디어
    - 좌 하 우 상 방향으로 bfs를 진행하면 가장 빠르게 도달하는 애가 방문 처리를 해버린다. -> 최단거리
    - 그래프의 값을 1씩 증가시키며 간다.
2. 시간복잡도
    - BFS -> O(V+E) 10000 + 4*10000 -> 50,000
3. 자료구조
    - N,M 크기로 주어지는 미로 -> int [][]
    - 방문 여부를 확인하기 위한 배열 -> bool [][]
    - 도달하는 경우를 전부 넣은 배열 -> int []
"""


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for _ in range(n):
    # 문자열 배열로 저장 후 정수형으로 변환
    # arr = list(input().strip()) + list(map(int, arr))
    # graph.append(list(map(int, list(input().strip()))))
    # 다른 블로그 글 찾아보니 굳이 위에 꺼로 안해도 되고
    # 그냥 input 자체를 int로 만들어서 배열화 화면 정수 배열이 된다.
    graph.append(list(map(int, input().strip())))


visited = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1 ,0]

def bfs():
    q = deque([(0,0)])

    while q:
        y, x = q.popleft()
        # 마지막에 도달했을 경우 리턴
        if y == n-1 and x == m-1:
            return graph[y][x]

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<m):
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((ny, nx))
    # 큐에 값이 없어졌을 때도 끝 값 리턴
    return graph[n-1][m-1]

print(bfs())
