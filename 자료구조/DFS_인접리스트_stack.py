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

def dfs(graph, i, visited):
    stack = [i]
    while stack:
        value = stack.pop()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True

        for c in graph[value][::-1]:
            if not visited[c]:
                stack.append(c)

dfs(graph, v, visited)

