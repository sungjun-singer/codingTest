"""
1. 아이디어
    - 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서
    - i에서 j로 가는 길이가 양수인 경로의 여부를 구하는 프로그램을 작성하시오
    - 인접 행렬이 주어지고, i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻.
    - 0인경우는 없다는 뜻
    - 그러면 방향이 있는 그래프인데 연결이 되어 있는지만 판단을 하는거기 때문에 dfs가 더 효율적이다.
    - dfs로 구현해보자
    - 인접 행렬은 많이 안접해봐서 추후에 하기로 하고 인접 리스트로 바꿔서 구현하자
2. 시간복잡도
    - 인접행렬 -> 인접리스트 변환 : N^2 -> 10000
    - DFS : O(V+E) -> 10000 + 4*10000 = 50000
3. 자료구조
    - 처음 입력 저장할 2차원 배열 -> int [][]
    - 리스트로 변환한 배열 -> int [][]
    - 방문 여부 -> bool []
"""

import sys
input = sys.stdin.readline

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

new_graph = [[] for _ in range(n+1)]
res = [[] for _ in range(n+1)]

def dfs(v, start):

    for k in new_graph[v]:
        if not visited[k]:
            res[start].append(k)
            visited[k] = True
            dfs(k, start)



for i in range(n):
    for j in range(n):
        if graph[i][j] ==1:
            new_graph[i+1].append(j+1)

real_res = [[0] * n for _ in range(n)]


for i in range(1,n+1):
    visited = [False] * (n+1)
    dfs(i, i)

for i in range(1, n+1):
    for x in res[i]:
        real_res[i-1][x-1] = 1


for x in real_res:
    print(" ".join(map(str, x)))