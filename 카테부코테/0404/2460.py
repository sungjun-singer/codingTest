"""
1. 아이디어
    - 20번의 승객 숫자를 배열에 저장하고 최대값을 출력한다.
2. 시간복잡도
    - 최대값 찾기 : O(n)
3. 자료구조
    - 승객 현황 배열 : int []
"""

import sys
input = sys.stdin.readline

# 처음 기차에 탑승 한 것 넣어주기
res = list(map(int, input().split()))

for _ in range(9):
    off, on = map(int, input().split())

    prev = res[-1]
    res.append(prev - off)
    res.append(prev - off + on)

print(max(res))

