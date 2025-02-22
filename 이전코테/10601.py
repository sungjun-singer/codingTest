import sys
input = sys.stdin.readline

n = input().strip()

if '0' not in n:
    print(-1)
else:
    sum_ = 0
    for i in range(len(n)):
        sum_ += int(n[i])

    if sum_ % 3 != 0:
        print(-1)
    else:
        arr = sorted(n, reverse=True)
        print(''.join(map(str, arr)))

