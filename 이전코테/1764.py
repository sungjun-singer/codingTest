n, m = map(int, input().split())

dic = set()
arr = []
res = []
for i in range(n):
    dic.add(input())

for _ in range(m):
    arr.append(input())

for x in arr:
    if x in dic:
        res.append(x)

res.sort()
print(len(res))
for x in res:
    print(x)