"""
1. 아이디어
    - N번째 피보나치 수를 구하는 문제인데
    - N이 20밖에 안되므로 그냥 재귀함수로 하자
    - DP는 더 클때 사용하면 된다.
    - F(n) = F(n-1) + F(n-2)
    - 연산횟수를 한번 세어보자
2. 시간복잡도
    - 이진 트리 형태로 퍼져 나가기 때문에 O(2^n)
3. 자료구조
    -
"""

import sys
input = sys.stdin.readline

n = int(input())

count = 0
def fibonacci(x):
    global count
    count += 1
    if x == 0:
        return 0
    if x == 1:
        return 1

    return fibonacci(x-1) + fibonacci(x-2)


print(fibonacci(n))
print(count)


"""
연산 횟수 f(n) = f(n-1) + f(n-2) + 1
1 3 5 9 15 25 41 67 109 177 287
"""
