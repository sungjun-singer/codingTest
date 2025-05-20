"""
1. 아이디어
    - 루트 없는 트리가 주어지고 루트가 1일때, 각 노드의 부모를 구하는 프로그램 작성
    - 일단 데이터를 먼저 넣고 지켜보자

2. 시간복잡도

3. 자료구조

"""


import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]


parent = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    q = deque([v])

    visited[v] = True

    while q:
        value = q.popleft()

        for k in graph[value]:
            if not visited[k]:
                visited[k] = True
                q.append(k)
                parent[k] = value

bfs(1)

for i in range(2, n+1):
    print(parent[i])

