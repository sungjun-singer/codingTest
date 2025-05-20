from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

for x in graph:
    x.sort()

def bfs(graph, i, visited):
    queue = deque([i])

    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True

        for c in graph[value]:
            if not visited[c]:
                queue.append(c)

def dfs(graph, i, visited):
    print(i, end=' ')
    visited[i] = True

    for c in graph[i]:
        if not visited[c]:
            dfs(graph, c, visited)

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)