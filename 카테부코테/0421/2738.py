"""
1. 아이디어
    - 행렬 두개를 같은 인덱스의 값을 더해서
2. 시간복잡도
    - O(n^2) : 이차원 배열 돌면서 원소들 더하기 해서 : 100 * 100 -> 10000
3. 자료구조
    - 이차원 배열 2개 : int [][]

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr1[i][j] += arr2[i][j]

for x in arr1:
    print(" ".join(map(str, x)))

