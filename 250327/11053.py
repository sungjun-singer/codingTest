"""
1. 아이디어
    - 가장 긴 증가하는 부분 수열을 구한다.
    - 예를 들어 {10, 20, 10, 30, 20, 50} 일 때, 1,2,4,6 을 해서 4개
    - 정렬은 안된다.
    - 거꾸로 시작해서 만약에 오른쪽에 더 큰 값들이 있다면 그 큰값들의 최대값 + 1을 저장
    - 없다면 1로 진행
2. 사간복잡도
    - O(n^2) -> 1000 * 1000 -> 1,000,000
3. 자료구조
    - 저장 배열 -> int []
    - 수열 값 저장 배열 -> int []
"""

import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

dp = [1] * n

# 거꾸로 진행하고
for i in range(n-1, -1, -1):
    flag = False
    arr = []
    # 순회할 숫자를 정하고
    for j in range(i, n):
        # 순회할 숫자의 오른쪽에 자신보다 큰 숫자가 있다면
        if numbers[i] < numbers[j]:
            # 있다고 하고
            flag = True
            # 큰 숫자의 인덱스를 저장
            arr.append(j)
    # 큰 숫자가 있는 경우
    if flag:
        # 큰 숫자에다가 1을 더한 값을 저장한다. ( 가장 긴 수열에다가 +1하는것)
        maxv = 0
        for x in arr:
            maxv = max(maxv, dp[x])
        dp[i] = maxv + 1

# 가장 긴 수열 출력
print(max(dp))