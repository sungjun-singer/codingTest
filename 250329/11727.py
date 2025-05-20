"""
1. 아이디어
    - 2*n 직사각형을 3가지 도형으로 채우는 경우의 수를 구하는 문제
    - 점화식은 f(n) = 2f(n-2) + f(n-1)
    - dp 배열에 저장해가며 진행한다.
2. 시간복잡도
    - O(n)
3. 자료구조
    - dp 배열 -> int []
"""

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    exit(0)

dp = [0] * (n+1)

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = 2*dp[i-2] + dp[i-1]


print(dp[n] % 10007)




