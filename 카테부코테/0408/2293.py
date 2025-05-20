"""
1. 아이디어
    - n가지 동전이 있는데 다 가치가 다르다.
    - 동전의 가치는 100000보다 작거나 같은 자연수
    - n개의 동전을 합쳐서 k가 되게 하는 경우의 수를 구하시오
    - 동전의 구성만 본다. 순서는 보지 않는다.
    - 제일 작은 수로만 1 * 10
    - 만약에 1 19 2가 나왔다면 0 출력이겠지
    - 주어진 테스트케이스로 일단 아이디어 떠올려보면
    - 1 10개로 했을 때
    - 1 8 2 1
    - 1 6 2 2
    - 1 4 2 3
    - 1 2 2 4
    - 1 0 2 5
    - 1 5 5 1
    - 1 0 5 2
    - 1 1 2 2 5 1
    - 일단 제일 작은걸로 0인 배열에 다 +1 해주고
    - 그 다음 작은 걸로 1과 0이 섞여 있는 배열에 dp[i-작은가치] + dp[i] + 1 해주면 최신화
2. 시간복잡도
    - O(n) 배열 하나만 도는 거
3. 자료구조
    - coins 배열 -> int []
    - dp 배열 -> int []
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]
dp = [0] * (k+1)

# 코인 크기 오름차순 정렬
coins.sort()

# k보다 큰 값 삭제
for coin in reversed(coins):
    if coin > k:
        coins.pop()


for coin in coins:
    # 초기 값 설정
    dp[coin] = dp[coin] + 1
    for i in range(coin+1, k+1):
        dp[i] = dp[i-coin] + dp[i]

print(dp[k])


