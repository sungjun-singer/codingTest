"""
1. 아이디어
    - 촌수 계산. 아버지는 1촌, 할아버지는 2촌, 형제는 3촌
    - 여러 사람들 간의 관계가 주어졌을 때, 두 사람의 촌수를 계산하는 프로그램을 작성하는건데
    - 전체 사람의 수 n, 촌수를 계산해야하는 서로 다른 두 사람의 번호가 주어지고
    - 셋째 줄에서는 관계의 개수 m, 그 아래에는 관계, x가 y의 부모
    - BFS로 구한다 최단 거리기 때문에
    - 원하는 노드에 도착했을 때 거리 배열에 저장해놓았던 거리 출력한다.
2. 시간복잡도
    - BFS -> O(V+E) : 50,000
3. 자료구조
    - 노드 별 이어져 있는 관계 배열 : int [][]
    - 노드의 방문 여부 -> int []
    - 거리 저장 배열 -> int []
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

p1, p2 = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n+1)

def bfs(v):
    q = deque([v])
    dist[v] = 0

    while q:
        val = q.popleft()

        if val == p2:
            print(dist[val])
            return

        for x in graph[val]:
            if dist[x] < 0:
                q.append(x)
                dist[x] = dist[val] + 1

    print(dist[p2])

bfs(p1)
