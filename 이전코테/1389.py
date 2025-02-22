"""
5(노드) 5(간선)
A B
1 3
1 4
4 5
4 3
3 2

5 5
1 3
1 4
4 5
4 3
3 2

케빈 베이컨 법칙
A, B는 친구고 B,A도 친구다
양방향 그래프

그래프 탐색을 하는 횟수를 다 더하고
그 횟수가 가장 작은 사람을 구하는 문제

1. 아이디어
- 일단 그래프를 만든다.
2. 시간복잡도

3. 자료구조
- 노드 : int[][]


"""

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    q = deque([start])

    while q:
        x = q.popleft()

        for i in graph[x]:
            if i not in visited:
                visited.append(i)
                q.append(i)
                num[i] = num[x] + 1

    return sum(num)

res = []
for p in range(1, (n+1)):
    res.append(bfs(graph, p))

print(res.index(min(res)) + 1)