"""
1. 아이디어
    -
2. 시간복잡도

3. 자료구조

"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

cmd = [input().strip() for _ in range(n)]

q = deque()

for x in cmd:
    if x.split()[0] == "push":
        q.append(x.split()[1])
    elif x.split()[0] == "pop":
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif x.split()[0] == "size":
        print(len(q))

    elif x.split()[0] == "empty":
        if len(q):
            print(0)
        else:
            print(1)
    elif x.split()[0] == "front":
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif x.split()[0] == "back":
        if len(q):
            print(q[-1])
        else:
            print(-1)







