from queue import PriorityQueue
import sys
input = sys.stdin.readline

q = PriorityQueue()

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for x in arr:
    if x != 0:
        q.put((abs(x), x))
    else:
        if q.qsize() == 0:
            print(0)
        else:
            print(q.get()[1])
