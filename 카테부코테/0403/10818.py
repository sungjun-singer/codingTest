"""
1. 아이디어
    - 정수의 최소값과 최대값을 구하는 문제?
2. 시간복잡도
    - 최소값과 최대값 구하는 거니깐 2*N -> O(N) 2,000,000
3. 자료구조
    - 숫자 저장 배열 -> int []
"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


print(min(arr), max(arr))

