"""
1. 아이디어
    - n가지 종류의 동전이 있고, 이걸 적당히 사용해 k원이 되도록 하는데 동전의 개수는 최소
    - 동전은 무제한으로 사용 가능하다.
    - n, k가 주어지고 아래에는 각각의 동전의 가치가 주어진다.
    - 이걸 하기 위해서는 DP를 써야할 거 같긴 하다.
    - 일단 k만큼의 배열을 만들어 둔다.
    - 그리고 각 동전을 더하면서 최소 값을 구하면서 진행한다.
    - 중복될 수 있다고 했으니 set으로 중복 제거 한 이후 배열로 진행한다.
    - 그리고 동전의 가치 > k 인 경우는 배열을 벗어나므로 삭제한다.
    - 가장 작은 동전의 가치만큼 k배열을 다 돌려놓고
    - 그다음 두번째 동전의 가치의 인덱스부터 시작을 하며 dp값을 더 작은 값으로 수정하면서 간다.
    - 두번째 동전으로 구할 수 없는 값일 때는 10001 + 1 이 되기 때문에 엄청 커져서 반영이 안된다.
2. 시간복잡도
    - O(k * n) -> 1,000,000
3. 자료구조
    - k 배열 : int [10000]
    - 동전의 가치 배열 : int [100]

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [100001] * (k+1)
dp[0] = 0
coins = [int(input()) for _ in range(n)]

# 같은 동전 값 중복 제거
coins = list(set(coins))

# 중복 제거 하면 정렬이 풀려서 다시 수행
coins.sort()

for coin in coins:
    for i in range(coin, k + 1):  # 현재 갖고 있는 동전 i를 기준으로 i 미만의 값은 갱신될리 없으므로 i부터 시작.
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])



