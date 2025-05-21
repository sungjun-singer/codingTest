import sys
input = sys.stdin.readline

n = int(input())
strings = []

for _ in range(n):
    strings.append(input().strip())

def is_vps(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                print("NO")
                return
            stack.pop()

    if len(stack) <= 0:
        print("YES")
    else:
        print("NO")

for str in strings:
    is_vps(str)