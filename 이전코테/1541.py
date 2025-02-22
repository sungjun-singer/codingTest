import sys
from curses.ascii import isdigit

input = sys.stdin.readline

str = input()

mode = False
res = 0
element = ''
for x in str:
    if isdigit(x):
        element += x
    else:
        if mode:
            res -= int(element)
            element = ''
        else:
            res += int(element)
            element = ''

    if x == '-':




        mode = True

print(res)