"""

1. 아이디어
    10
    10 -4 3 1 5 6 -35 12 21 -1
    - 여기서 연속된 숫자들의 합이 최대가 되게 구하는건데
    - dp 배열을 하나 더 만들어서
    - 앞에 숫자들을 더했을 때 양수가 나온다면 양수로 놓고 아니라면 0으로 놔둔다
    - 예를들어 -35를 했을 때 음수가 되면 배열은 0으로 두고 진행
2. 시간복잡도

3. 자료구조

"""

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))