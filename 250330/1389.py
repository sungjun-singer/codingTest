"""
1. 아이디어
    -
2. 시간복잡도

3. 자료구조

"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

people = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

new_people = []

for x in people:
    set1 = set(x)
    x = list(set1)
    new_people.append(x)

def bfs(v):
    q = deque([v])

    while q:
        val = q.popleft()

        for k in new_people[val]:
            if not visited[k]:
                q.append(k)
                visited[k] = visited[val] + 1

res = []
for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)

    res.append(sum(visited) - visited[i])

print(res.index(min(res)) + 1)