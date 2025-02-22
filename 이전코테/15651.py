import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []

def recur(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, n+1):
        res.append(i)
        recur(i)
        res.pop()

recur(1)