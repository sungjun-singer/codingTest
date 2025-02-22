import sys
input = sys.stdin.readline

arr = []

n = int(input())
for _ in range(n):
    d, w = map(int, input().split())
    arr.append((w,d))


visited = [False] * 1001
res = 0
arr.sort(reverse=True)

for x in arr:
    (w,d) = x
    while d > 0:
        if not visited[d]:
            visited[d] = True
            res += w
            break
        else:
            d -= 1

print(res)


