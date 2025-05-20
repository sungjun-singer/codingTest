from collections import deque

s, e = map(int, input().split())

t = 0
if s == e:
    print(t)
else:
    Q = deque()
    V = set()

    if s == 0:
        s = 1
        t = 1
        V.update([0, 1])

    Q.append((s, t))
    V.add(s)

    while Q:
        x, t = Q.popleft()

        if x == e:
            break
        for nx in (2*x, x-1, x+1):

            if (0<=nx<=100000):
                if nx not in V:
                    V.add(nx)
                    if nx == 2*x:
                        Q.appendleft((nx, t))
                    else:
                        Q.append((nx, t+1))

    print(t)