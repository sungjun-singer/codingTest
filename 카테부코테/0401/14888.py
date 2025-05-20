"""
1. 아이디어
    - N개의 수와 N-1개의 연산자
    - 수와 수 사이에 연산자를 넣어서 수식을 하나 만들 수 있다.
    - 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행한다.
    - 주어졌을 때 최소인것과 최대인 것을 구하는 프로그램을 작성하시오
    - 연산자의 개수는 알아서 주어지고
    - 작은수를 빼고 큰수를 더하거나 곱하면 되는데
    -
2. 시간복잡도

3. 자료구조

"""

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    # 모든 숫자를 다 썼다면 전체 total 값이랑 min, max 값이랑 비교해서 새로 저장
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # 각 연산자가 남아있을 경우(0이 아닐 경우) 수행
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)