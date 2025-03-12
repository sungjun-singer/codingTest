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

print(graph)

def dfs(graph, i, visited):
    print(i, end=' ')
    visited[i] = True

    for c in graph[i]:
        if not visited[c]:
            dfs(graph, c, visited)

dfs(graph, v, visited)

