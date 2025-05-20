"""
1. 아이디어
    - 서로다른 N개의 자연수의 합이 S
    - 1부터 진행해야 최대값이 나올거니깐
    - 1부터 하나씩 더하면서 count가 몇개가 되었는지 세면 되겠다.
    - 파이썬이라 큰 수는 고려하지 않아도 된다.
2. 시간복잡도
    - 4294,967,295는 몇개를 더해야 되는거지?
3. 자료구조
    - 정수 변수 : count
"""

import sys
input = sys.stdin.readline

S = int(input())

sum = 0
cnt = 0
i = 1

while True:
    sum += i

    if sum > S:
        break
    cnt += 1
    i += 1

print(cnt)