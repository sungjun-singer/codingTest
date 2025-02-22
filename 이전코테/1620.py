n,m = map(int, input().split())

set1 = {}
arr = []

for i in range(1, n+1):
    set1[i] = input()

reverse_set1 = {v:k for k,v in set1.items()}

for x in range(m):
    problem = input()
    if problem.isdigit():
        arr.append(int(problem))
    else:
        arr.append(problem)

for x in arr:
    if type(x) == int:
        print(set1.get(x))
    else:
        print(reverse_set1.get(x))



