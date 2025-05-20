import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    exit(0)

visited = set()

def bfs(start, cnt):
    if start == 0:
        cnt += 1
        start = 1
        visited.update([0, 1])

    q = deque()

    q.append((start, cnt))

    while q:
        cur, cnt = q.popleft()

        if cur == k:
            return cnt

        for nx in (cur*2, cur-1, cur+1):
            if (0<=nx<=100000) and nx not in visited:
                visited.add(nx)
                if nx == (cur*2):
                    q.appendleft((nx, cnt))
                else:
                    q.append((nx, cnt+1))


print(bfs(n, 0))