"""
1. 아이디어
    - 최대가 되는 경우를 어떻게 파악할까?
    - 3개 연속으로 마실 수는 없어
    - 6 10 13 9 8 1
    - 점화식 dp[i] = arr[i] + max(dp[i-2], dp[i-3] + arr[i-1])
2. 시간복잡도
    - O(n)
3. 자료구조
    - 포도잔 배열 : int []
    - dp 배열 : int []
"""

import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
dp = [0] * n

if n == 1:
    print(arr[0])
    exit(0)
if n == 2:
    print(arr[0] + arr[1])
    exit(0)

dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1])


for i in range(3, n):
    # dp[i-1]의 잔이 더 크면 그냥 현재 잔 안먹는걸로 해서 현재 잔을 dp[i-1]로 진행
    dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(max(dp))
