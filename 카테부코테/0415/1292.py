"""
1. 아이디어
    - a부터 b까지 더하는데
    - 1 2 2 3 3 3 4 4 4 4 이렇게 숫자별로 반복된 수열에서 합을 구하면 된다.
    - 1000개까지가 끝이니 그냥 배열을 만들어 놓고 인덱스 a부터 b까지 더하면 된다.
2. 시간복잡도
    - O(n)
3. 자료구조
    - 수열 저장 배열 : int []
    - 정수 저장 변수 : int
"""

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 1000 이면 몇 팩토리얼이지?
# 46까지면 1035가 나와서 1035까지 배열 만들어두고 계산
arr = []
for i in range(1, 47):
    for j in range(0, i):
        arr.append(i)

res = 0
for i in range(a-1, b):
    res += arr[i]

print(res)