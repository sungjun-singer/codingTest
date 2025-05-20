import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
visited = set()

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x, cnt):
    global answer

    visited.add(graph[y][x])

    answer = max(answer, cnt)

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (0<=ny<r) and (0<=nx<c):
            if not graph[ny][nx] in visited:
                visited.add(graph[ny][nx])
                dfs(ny, nx, cnt+1)
                visited.remove(graph[ny][nx])



answer = 0

dfs(0,0,1)

print(answer)