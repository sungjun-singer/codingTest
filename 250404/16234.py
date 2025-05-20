"""
1. 아이디어
    - 상하좌우 돌면서 visited가 False이고, 현재칸과 이동할 칸의 차이가 L이상 R이하인 경우 탐색
    - 탐색이 될 경우 visited = True로 바꾸고, sum에 현재 칸의 값을 더하고, cnt값을 1증가 시킨다.
    - bfs가 끝나고 cnt 값이 2 미만이면 res를 리턴해주고
    - cnt값이 2이상이면 visited가 True인 칸에 sum // cnt 값을 넣는다.
    - 계속 반복
2. 시간복잡도
    - bfs -> O(V+E) -> 5*50*50 -> 12500 인데 인구 이동 발생하는 일수가 2000이하
    - 그러면 12500 * 2000번동안 이동하니깐 25,000,000 이고, 1초에 2천만번이니 2초면 4천만번 -> 가능
3. 자료구조
    - 인구 저장 배열 : int [50][50]
    - 방문 여부 배열 : bool [50][50]
    - 각종 정수 저장 변수들 : int
"""

import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    # 이어지는 나라 인구수 총합
    sum_ = 0
    # 좌표값 저장 하기 위한 배열
    tmp = []

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if (0<=ny<n) and (0<=nx<n):
                diff = abs(graph[ny][nx] - graph[y][x])
                # 방문하지 않았고, 인구 차이가 l 이상 r 이하인경우
                if not visited[ny][nx] and (l <= diff <= r):
                    # 방문 처리
                    visited[ny][nx] = True
                    # 좌표 저장
                    tmp.append((ny, nx))
                    # 인구수 합치기
                    sum_ += graph[ny][nx]
                    # 다음 탐색으로 큐에 넣기
                    q.append((ny, nx))
    # 길이 저장
    length = len(tmp)
    # 길이가 0이 아닐 경우
    if length:
        # 국경이 연결된 나라 좌표에 인구수 평균값 넣기
        for element in tmp:
            y, x = element
            graph[y][x] = (sum_ // length)

    # 바뀐 값이 몇개인지 리턴(밖의 while true break 하는 용도)
    return length


day = 0
while True:
    # 방문 배열 초기화(문제에서의 다음날)
    visited = [[False] * n for _ in range(n)]

    max_value = 0
    # 반복문 순회
    for i in range(n):
        for j in range(n):
            # 방문하지 않은 노드가 있다면 bfs 시작
            if not visited[i][j]:
                # 리턴된 값중 가장 큰 값 저장(만약 0이라면 반복문 종료)
                max_value = max(bfs(i, j), max_value)

    # 0이라면 day 출력 하고 종료
    if not max_value:
        print(day)
        break

    day += 1























