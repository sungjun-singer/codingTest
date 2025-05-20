from collections import deque

import sys
input = sys.stdin.readline

n,m,v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    f,t = map(int, input().split())
    matrix[t][f] = matrix[f][t] = 1

print(matrix)


def bfs(matrix, i, visited):
    queue = deque()
    queue.append(i)
    while queue:
        value = queue.popleft()
        if not visited[value]:
            print(value, end=' ')
            visited[value] = True

        for c in range(len(matrix[value])):
            if matrix[value][c] == 1 and not visited[c]:
                queue.append(c)

bfs(matrix, v, visited)



bfs(matrix, v, visited)