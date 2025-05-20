"""
1. 아이디어
    - 정수 A를 B로 바꿀려고 한다.
    - 가능한 연산은 두가지이다. 2를 곱한다. 1을 수의 가장 오른쪽에 추가한다.
    - 다음 연산 2개로 해두고 최소거리를 출력해야하기 때문에 BFS를 수행한다.
    - 다음 연산이 목표 값보다 크면 큐에 넣지 않는다.
    - 이 상태로 진행
2. 시간복잡도
    - BFS -> O(V+E) -> 2^30이 10**9보다 크다 그럼 깊이가 30이 되는거고 b보다 커지는 경우 사라지기 때문에
    - 1만 계속 붙이는 경우는 10번정도 진행하면 더이상 큐에 넣지 않고 2곱하고 계속 1만 붙이는 경우는 11번
    - 그러고 2만 계속 붙이는 경우는 31번 정도 진행하니깐 시간복잡도가 오바가 되진 않을거 같다.
3. 자료구조

"""

# i = 1
#
# cnt = 0
# while i < 10**9:
#     cnt += 1
#     i = i*2
#
# print(cnt)


import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())


def bfs(v, cnt):

    q = deque([(v, cnt)])

    while q:
        x, cnt = q.popleft()

        for nx in (x*2, int(str(x)+'1')):
            if nx < b:
                q.append((nx, cnt+1))
            elif nx == b:
                print(cnt+1)
                return

    print(-1)

bfs(a, 1)






