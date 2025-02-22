import sys
input = sys.stdin.readline

n = int(input())

memo = [0] * (n+1)

for i in range(2, n+1):
    if i % 6 == 0:
        memo[i] = min(memo[i // 3] + 1, memo[i // 2] + 1, memo[i - 1] + 1)
    elif i % 3 == 0:
        memo[i] = min(memo[i//3] +1, memo[i-1] + 1)
    elif i % 2 == 0:
        memo[i] = min(memo[i//2] + 1, memo[i-1] + 1)
    else:
        memo[i] = memo[i-1] + 1

print(memo[n])

