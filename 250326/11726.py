"""
1. 아이디어
    - 피보나치 수열의 규칙을 가진다.
2. 시간복잡도
    - O(n) -> 1000
3. 자료구조
    - 1000까지의 숫자를 저장해둔 배열 -> int []
"""

import sys
input = sys.stdin.readline

n = int(input())

arr = [0, 1, 2] + [0] * (n-2)

for i in range(3, n+1):
    arr[i] = arr[i-2] + arr[i-1]

print(arr[n] % 10007)
