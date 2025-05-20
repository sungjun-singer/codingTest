"""
1. 아이디어
    - 다리를 지을 수 있는 경우의 수
    - 1 1 일때는 1개
    - 1 2 일때는 2개
    - 1 3 일때는 3개
    - 2 1 일때는 1개
    - 2 2 -> 1
    - 2 3 -> 3
    - 2 4 -> 6
    - 2 5 -> 10
    - 3 3 -> 1
    - 3 4 -> 4
    - 3 5 -> 10

    - 1 1 -> 1 / 1 2 -> 2 / 1 3 -> 3
    - 2 2 -> 1 / 2 3 -> 3 / 2 4 -> 6 / 2 5 -> 10
    - 3 3 -> 1 / 3 4 -> 4 / 3 5 -> 10

    - (i, j) = (i-1)(j-1) + (i)(j-1) 로 볼 수 있다.

2. 시간복잡도
    -
3. 자료구조

"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    res = 1

    # 큰수 팩토리얼
    for i in range(m):
        res *= (i+1)

    # 작은 수 팩토리얼
    for i in range(n):
        # 1, 2, 3
        res //= (i+1)

    # 큰 수 - 작은 수 팩토리얼
    for i in range(m-n):
        # 2, 1
        res //= (i+1)

    print(res)