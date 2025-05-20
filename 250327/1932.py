"""
1. 아이디어
    - 크기가 5인 정수 삼각형
    - 위에서 부터 내려오는데, 대각선 오른쪽과 대각선 왼쪽에 있는 수만 선택해서 내려올 수 있고
    - 가장 최대값을 만들면서 내려와야 한다.
    - 어떻게 해야할까
    - 아래 친구 입장에서 위에서 더 큰 놈을 선택해서 자기랑 더한다.
2. 시간복잡도
    - O(n^2) -> 500 * 500 -> 250,000
3. 자료구조
    - 삼각형 배열 -> int [][]
    - dp 배열 -> int [][]
"""

import sys
input = sys.stdin.readline

n = int(input())

triangle = []



for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = []

for i in range(1, n+1):
    arr = [0] * i
    dp.append(arr)



dp[0][0] = triangle[0][0]

for i in range(1, n):
    # 양 끝 더해주기
    dp[i][0] = dp[i-1][0] + triangle[i][0]
    dp[i][i] = dp[i-1][i-1] + triangle[i][i]

    for j in range(1, len(triangle[i])-1):
        dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))