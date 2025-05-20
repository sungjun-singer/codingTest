"""
1. 아이디어
    - 연결요소의 개수
    - 전부 다 연결되어 있으면 1 출력
    - 끊어져 있어 여러 요소로 나뉘면 2이상 출력
2. 시간복잡도
    - DFS -> O(V+E) N+M 1000 + 999*500 : 500500
3. 자료구조
    - 노드와 간선의 개수 : n, m
    - 노드와 간선의 배열 : int [][]
"""

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

def dfs(v):

    visited[v] = True

    for x in graph[v]:
        if not visited[x]:
            dfs(x)


cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)

