"""
1. 아이디어
    - 두 자연수가 주어지는데 이 둘의 최소공배수와 최대공약수를 구하라
    - 라이브러리를 사용하면 편하긴 할텐데 라이브러리를 사용하지 않고 해보자
    - 찾아봤는데, 작은 숫자부터 시작해서 i를 -1씩 하며 둘다 나누어 떨어지는(a%i, b%i) 거가 최대공약수이고
    - 큰 숫자부터 시작해서 두 수를 곱한수까지 i를 +1씩 하며 둘다 나누어 떨어지는(i%a, i%b)거가 최소공배수
2. 시간복잡도
    - 만약 10000 * 10000 이면 1억, 그러면 1억번 반복 하면 시간복잡도가 될려나
    - 파이썬은 1초에 2000만번이니 불가능하다. 아마 시간초과가 날듯
    - 안 나네, 왜일까
3. 자료구조

"""

import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())

# 최대공약수
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소공배수
for i in range(max(a, b), (a*b)+1):
    if i%a == 0 and i%b == 0:
        print(i)
        break


