import sys
input = sys.stdin.readline

n, m, v = map(int,input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int,input().split())
    matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
    stack = [i]
    while stack:
        element = stack.pop()

        if not visited[element]:
            print(element, end=' ')
            visited[element] = True

        for c in range(len(matrix[element])-1, -1, -1):
            if matrix[element][c] == 1 and not visited[c]:
                stack.append(c)

dfs(matrix, v, visited)