"""
1. 아이디어
    - 배열 A가 주어졌을 때 N번째 큰 값을 출력하는 프로그램 작성
    - 배열의 크기는 항상 10이고, 자연수만 가지고 있다. N은 항상 3이다.
2. 시간복잡도
    - 정렬 O(nlogn) 10(n)*4(logn) * 1000(T)
3. 자료구조
    - 배열 : int [10]
"""

import sys
input = sys.stdin.readline

T= int(input())

for _ in range(T):
    arr = list(map(int, input().split()))

    arr.sort()
    print(arr[7])

