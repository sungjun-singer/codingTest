n = int(input())
arr = []
cnt = 0
stack = []
res = []


for _ in range(n):
    arr.append(int(input()))

while n >= cnt:
    for x in arr:
        if x >= cnt:
            for i in range(cnt+1, x + 1):
                stack.append(i)
                res.append("+")
            cnt += x-cnt
        if len(stack) == 0:
            for ans in res:
                print(ans)
            exit(0)
        ele = stack.pop()
        if ele is not x:
            print("NO")
            exit(0)
        res.append("-")