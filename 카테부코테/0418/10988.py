"""
1. 아이디어
    - 앞으로 읽을때와 거꾸로 읽을 때 똑같은 단어
    - 문자열 뒤집어도 같은 문자열이면 1 아니면 0
2. 시간복잡도

3. 자료구조

"""

import sys
input = sys.stdin.readline

s = input().strip()

arr = list(s)

reverse_s = ''.join(map(str, reversed(arr)))


if s == reverse_s:
    print(1)
else:
    print(0)

