from queue import PriorityQueue
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
q = PriorityQueue()

problem = [False] * (N+1)
res = []

for _ in range(M):
    a, b = map(int, input().split())
    q.put((a,b))

for _ in range(M):
    p1, p2 = q.get()
    problem[p1] = problem[p2] = True
    res.append(p1)
    res.append(p2)

for i in range(1, N+1):
    if not problem[i]:
        res.append(i)

print(" ".join(map(str, res)), end='')