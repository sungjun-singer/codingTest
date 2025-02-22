import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
cmd = []
res = []

for _ in range(n):
    cmd = int(input())
    if cmd > 0:
        heapq.heappush(heap, (-cmd, cmd))
    else:
        if len(heap):
            res.append(heapq.heappop(heap)[1])
        else:
            res.append(0)

for x in res:
    print(x)




