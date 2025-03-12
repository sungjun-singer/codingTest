import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
    visited[i] = True
    print(i, end=' ')

    for c in range(len(matrix[i])):
        if matrix[i][c] == 1 and not visited[c]:
            dfs(matrix, c, visited)

dfs(matrix, v, visited)