import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

is_virus = [0] * (n+1)

def dfs(start):
    if is_virus[start]:
        return
    is_virus[start] += 1
    for element in arr[start]:
        if is_virus[element] == 0:
            dfs(element)

dfs(1)
print(sum(is_virus) - 1)

