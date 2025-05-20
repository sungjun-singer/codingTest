"""
1. 아이디어
    - 점화식을 찾아낸다.
    - 이 경우에는 arr[i] = arr[i-3] + arr[i-2] + arr[i-1]이다.
    - 배열에다가 저장하고 값을 구하면 끝
2. 시간복잡도
    - O(n) -> 11
3. 자료구조
    - 피보나치 수열 -> int []

"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    arr = [1,2,4] + [0] * (n-3)

    for i in range(3, n):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]

    print(arr[n-1])