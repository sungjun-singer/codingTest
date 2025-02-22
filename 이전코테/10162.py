import sys
input = sys.stdin.readline

n = int(input())
res = []

if n % 10 != 0:
    print(-1)
    exit(0)

res.append(n // 300)
n %= 300
res.append(n // 60)
n %= 60
res.append(n // 10)

print(' '.join(map(str, res)))