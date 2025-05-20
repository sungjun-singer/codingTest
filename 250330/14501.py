"""
1. 아이디어
    - 1일꺼를 했을 때 : 2,3일꺼는 못한다. dp[1]만 10이고 dp[4] 10으로 놔둬
    - 2일꺼를 했을 때 : 3,4,5,6일꺼 못한다 dp[2]만 20이고 dp[7] 20으로 둬
    - 3일꺼를 했을 때 : 못하는 거 없음 dp[3]을 10으로 두고 dp[4]는 더 큰값을 채택하는데 10과 10은 같으니 그냥 유지
    - 4일꺼를 했을 때 : 못하는거 없음 dp[4] = dp[4] + 20 / dp[5] = dp[4]
    - 5일꺼를 했을 때 : 못하는거 6일꺼 dp[5] = dp[5] + 15 / dp[7] = dp[5]
    - 6일꺼를 했을 때 : 불가능함. 퇴사해야하기 때문
    - 7일꺼를 했울 때 : 불가능함. 퇴사해야하기 때문

    - 상담을 할때 현재 날짜에 point만큼 더하고, 현재 날짜 + 소요되는 날짜 부터 마지막 날까지 dp 배열에 있는 것과 비교해서 큰 값 채택

2. 시간복잡도
    - O(N) : N개수만큼 배열을 선형적으로 이동하면 되기 때문

3. 자료구조
    - 상담 배열 : int []
    - DP 배열 : int []
    - 각종 변수들 : int
"""

import sys
input = sys.stdin.readline

n = int(input())

counsel = []
dp = [0] * n

for _ in range(n):
    a, b = map(int, input().split())
    counsel.append((a,b))


for i in range(n):
    day, point = counsel[i]

    # 퇴사하는 날짜 넘어가면 진행하지 않음
    if i + day > n:
        continue

    # 현재 상담일에 이익 올리기
    dp[i] = dp[i] + point

    # 현재 상담일 + 소요일 부터 퇴사하는 날까지 가장 돈 많이 받을 수 있는 값 저장
    for j in range(i+day, n):
        dp[j] = max(dp[i], dp[j])

print(max(dp))