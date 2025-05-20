"""
1. 아이디어
    - 그냥 연결된 노드의 개수를 출력하면 되는듯
    - DFS로 풀자
2. 시간복잡도
    - DFS -> O(V+E) -> O(100 + 4950) -> O(5050)
    - 정점의 개수 : 100
    - 최대 간선의 개수 : 100*99 / 2 -> 50 * 99 -> 4950
3. 자료구조
    - 컴퓨터간의 관계 배열 : int [][]
"""

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)


def dfs(v):

    global count
    # 감영된 컴퓨터 방문처리
    visited[v] = True
    # 감영된 컴퓨터 숫자 증가
    count += 1

    # 연결된 컴퓨터 중
    for k in graph[v]:
        # 감영되지 않은 컴퓨터
        if not visited[k]:
            # 감염 시작
            dfs(k)

count = 0

dfs(1)
# 1번 컴퓨터도 포함해서 count를 세기 때문에 -1 해준다.
print(count-1)
