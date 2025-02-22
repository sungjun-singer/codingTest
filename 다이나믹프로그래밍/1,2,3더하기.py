# 9095번
"""
1. 아이디어
    - 1~6까지 숫자를 세어본 결과 피보나치 수열인데 이전 3개를 더하면 되었다.
    - 1 2 4 7 13 24
2. 시간복잡도
    - 배열 도는거라 O(n) = 11
    - 입력 T개

3. 자료구조
    - 정수 T, x
    - 배열 memo[], arr[]
"""

import sys
input = sys.stdin.readline

T = int(input())

memo = [1,2,4] + [0] * 7

for i in range(3, 10):
    memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

arr = []

for _ in range(T):
    x = int(input())
    arr.append(x)

for x in arr:
    print(memo[x-1])


