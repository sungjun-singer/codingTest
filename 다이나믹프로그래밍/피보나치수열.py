# 2748번
import sys
input = sys.stdin.readline

n = int(input())

memo = [1, 1] + [0] * (n-2)

for i in range(2, n):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n-1])