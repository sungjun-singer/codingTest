from collections import deque

q = deque()
n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

for x in arr:
    cmd = x.split()[0]
    if cmd == "push":
        q.append(int(x.split()[1]))
    elif cmd == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif cmd == "size":
        print(len(q))
    elif cmd == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif cmd == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])

