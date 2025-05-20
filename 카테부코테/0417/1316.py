"""
1. 아이디어
    - 알파벳이 처음 나왔을 때 상태를 알파벳으로 바꿔두고 집합에 넣기
    - 집합에 있는 알파벳이 나왔을 때 상태에 있는 알파벳이랑 다르다면 X
    - 끝까지 잘 진행된다면 + 1
2. 시간복잡도
    - 집합에 넣는 연산 : O(1)
    - 집합에서 요소 찾는 연산 : O(1)
    - 반복 횟수 : n = 100, 단어 길이 n = 100 -> 10,000
3. 자료구조
    - 단어 저장 집합 : set {}
    - 단어들 저장 배열 : str []
"""

import sys
from math import trunc

input = sys.stdin.readline

n = int(input())

arr = [input() for _ in range(n)]

res = 0

for x in arr:
    s = set()
    status = "init"
    for i in x:
        if i not in s:
            status = i
            s.add(i)
        else:
            if i != status:
                status = False
                break
    if status:
        res += 1

print(res)

