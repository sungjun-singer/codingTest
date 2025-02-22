a, b = map(int, input().split())

cnt = 0
while a != b:
    if a > b:
        print(-1)
        exit(0)
    if b % 10 == 1:
        b = b // 10
        cnt += 1
    else:
        if b % 2 == 0:
            cnt += 1
            b = b // 2
        else:
            print(-1)
            exit(0)


print(cnt+1)