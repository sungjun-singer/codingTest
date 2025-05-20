"""
1. 아이디어
    - 스택을 구현한다.
    - 1은 push 연산
    - 2눈 pop 연산 뺄게 없다면 -1 출력
    - 3은 스택의 길이 리턴
    - 4는 비어있는지 확인 1, 0
    - 5는 맨 위의 수 출략, 없다면 -1 출력
2. 시간복잡도
    - O(n)
3. 자료구조
    - 스택용 배열 : int []
"""

import sys
input = sys.stdin.readline

n = int(input())

command = list(input().strip() for _ in range(n))

stack = []

for x in command:
    if x[0] == '1':
        a, b = x.split()
        stack.append(b)
    elif x[0] == '2':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif x[0] == '3':
        print(len(stack))
    elif x[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == '5':
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
