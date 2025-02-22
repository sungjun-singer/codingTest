"""
8 9
0 0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0 0
0 0 0 1 1 0 1 1 0
0 0 1 1 1 1 1 1 0
0 0 1 1 1 1 1 0 0
0 0 1 1 0 1 1 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

두 면이 노출되어 있다면 사라진다.

visited[][] 는 boolean으로 두고
expose[][] int 배열로 만들어서 노출되는 숫자 쓰기
outside[][] 만들어서 공기에 노출되는 부분 표시하기
"""

from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
is_outside = [[False] * m for _ in range(n)]

def is_out(graph):
    q = deque([(0, 0)])
    is_outside[0][0] = True

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if graph[ny][nx] == 0 and not is_outside[ny][nx]:
                is_outside[ny][nx] = True
                q.append((ny,nx))

def arr_sum(graph):
    result = 0
    for x in graph:
        result += sum(x)

    return result

def is_end(graph):
    for x in graph:
        if sum(x) != 0:
            return True
    return False


def bfs(y, x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if graph[ny][nx] == 0 and not visited[ny][nx] and is_outside[ny][nx]:


            return


