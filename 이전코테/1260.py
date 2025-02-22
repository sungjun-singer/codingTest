"""
특정노드를 기준으로 연결된 모든 요소를 찾는 BFS 공식
응용 포인트1: visited를 bfs()가 아닌 solution() 에서 생성한다.
응용 포인트2: 특정 노드를 기준으로 연결된 모든 요소를 탐색한다.
응용 포인트3: 문제에서 특정 이동 조건을 제시하는 경우 사용한다.
응용 포인트4: 모든 노드를 순회하며 특정 노드의 기준점을 잡는다.
응용 포인트5: solution() 에서도 이동조건을 검사하며, bfs() 결과를 최종 결과에 추가한다.
"""

from collections import deque

def bfs(start_y, start_x, graph, visited):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    n, m = len(graph), len(graph[0])
    visited[start_y][start_x] = True

    # 연결된 component 배열
    component = []
    queue = deque([(start_y, start_x)])
    while queue:
        y, x = queue.popleft()
        component.append((y,x))

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= ny < n and 0 <= nx < m:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

    return component

def solution(graph):
    n, m = len(graph), len(graph[0])
    visited = [[False] * m for _ in range(n)]

    answer = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                answer.append(bfs(i, j, graph, visited))
    return answer

graph = [
    	['O', 'O', 'O', 'O', 'O', 'X'],
        ['O', 'O', 'O', 'O', 'X', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O', 'O', 'O'],
        ['X', 'O', 'O', 'O', 'O', 'O'],
    ]

print(solution(graph))