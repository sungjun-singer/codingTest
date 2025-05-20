"""
1. 아이디어
    - DFS와 BFS를 수행한 결과를 출력한다.
    - 시작하는 정점에서 작은 순서대로 방문한다.
2. 시간복잡도
    - DFS -> O(V+E) -> 11000
    - BFS -> O(V+E) -> 11000
    - 정렬 -> nlogn 인데, 총 간선의 개수는 10000개인데 ( 평균적으로 20개씩 배열에 들어있다면 80 * 1000 -> 80000이고 최악의 경우가 두개에 다 들어갔을 경우인데
    - 이렇게 그러면 10000 * 16 -> 160000 * 2 -> 320000
3. 자료구조
    - 정점과 간선의 배열 int [][], 밖에가 안의 요소의 총 개수가 10000개 가능이다.
    -
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 그래프 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for x in graph:
    x.sort()


def dfs(v):
    # 정점 방문 처리 및 출력
    visited[v] = True
    print(v, end=' ')

    # 정점과 연결된 노드 확인 후 방문하지 않았다면 방문 시작
    for k in graph[v]:
        if not visited[k]:
            dfs(k)

def bfs(v):
    # 큐에 첫 정점 넣기
    q = deque([v])

    # 큐가 빌때까지 반복
    while q:
        # 큐에 있는 정점 꺼내고
        a = q.popleft()

        # 정점이 방문하지 않은 정점이라면 방문처리하고 출력
        if not visited[a]:
            visited[a] = True
            print(a, end=' ')

        # 정점과 연결된 정점들 중에 방문하지 않은 정점 큐에 넣어 다음 방문지로 지정
        for k in graph[a]:
            if not visited[k]:
                q.append(k)

dfs(v)
print()
visited = [False] * (n+1)
bfs(v)


