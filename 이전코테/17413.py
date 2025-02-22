import sys
input = sys.stdin.readline

str1 = input().rstrip()
stack = []
is_switch = True
res = ''

for char in str1:
    if char == '<':
        while len(stack):
            res += stack.pop()
        res += char
        is_switch = False
    elif char == '>':
        is_switch = True
        res += char
    elif char == ' ':
        if is_switch:
            while len(stack):
                res += stack.pop()
            res += ' '
        else:
            res += ' '
    else:
        if is_switch:
            stack.append(char)
        else:
            res += char

while len(stack):
    res += stack.pop()

print(res)



