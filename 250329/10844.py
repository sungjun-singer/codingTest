# """
# 1. 아이디어
#     - 한자리수 9 두자리수 17 세자리수 32 네자리수 61
#     - 점화식 뽑아보면
#     - f(n) = 2*f(n-1) - n + 1
# 2. 시간복잡도
#     - O(n)
# 3. 자료구조
#     - 숫자들 : int
#     - dp 배열 : int []
# """
#
# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# dp = [0] * n
#
# dp[0] = 9
#
#
#
# for i in range(1, n):
#
#
# print(dp)
# print(dp[n-1]%(10**9))