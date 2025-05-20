"""
1. 아이디어
    - 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
    - 0 0 0 1 0 1 1 1 2 2
    - 점화식 P[i] = P[i-1] + P[i-5]
    - 그냥 100까지 다 만들어놓고 출력
2. 시간복잡도
    - O(n) -> 100
3. 자료구조
    - 삼각형 한변 길이 저장 배열 -> int []
"""

import sys
input = sys.stdin.readline

P = [1,1,1,2,2] + [0] * 95

for i in range(5, 100):
    P[i] = P[i-1] + P[i-5]

T = int(input())

for _ in range(T):
    n = int(input())

    print(P[n-1])