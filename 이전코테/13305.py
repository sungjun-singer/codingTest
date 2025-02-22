import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
spot = list(map(int, input().split()))

distance.append(0)

i = 0
res = 0

while i <= (n-1):
    cnt = 1
    for j in range(i+1, n):
        if spot[j] >= spot[i]:
            cnt += 1
        else:
            break
    tmp = 0
    for k in range(cnt):
        tmp += distance[i+k]
    res += (spot[i] * tmp)
    i += (cnt -1)
    i += 1

print(res)