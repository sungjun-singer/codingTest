"""
1. 아이디어
    - RGB 거리에는 집에 N개 있고, 1~N까지 순서대로 있다.
    - R, G, B 중 하나의 색으로 칠해야 하는데
    - 1번집의 색은 2번집의 색과 같지 않아야 하고
    - N번 집의 색은 N-1번 집의 색과 같지 않아야한다.
    - i 번째 집의 색은 i-1, i+1 집의 색과 같지 않아야한다.
    - 첫째 줄에 집의 수가 주어지고, 각 집을 칠하는 비용이 나타난다. 최소 비용을 출력해야한다.

    - 첫번째 R을 선택했을 때, 두번째에서는 G, B 중 하나만 선택, 세번째에서는 두번째에서 선택 안한 2가지 색상
    - 배열로 진행하고 이전 선택 인덱스를 기억하고 있다가 다음꺼는 그거 빼고 진행하기
    - 근데 최적의 해를 보장하지 않아. 1 2 1보다 2 1 2가 더 작을수도 있잖아
    - +
2. 시간복잡도
    - O(n) -> 3*1000 -> 3000
3. 자료구조
    - 집의 번호와 색상 저장 배열 -> int [][3]
    - dp 배열 -> int [][3]
    - 집의개수, 이전값 prev -> int
"""

import sys
input = sys.stdin.readline

n = int(input())

paints = []

for _ in range(n):
    paints.append(list(map(int, input().split())))

dp = [paints[0]]

for i in range(1, n):
    red = paints[i][0] + min(dp[i-1][1], dp[i-1][2])
    green = paints[i][1] + min(dp[i-1][0], dp[i-1][2])
    blue = paints[i][2] + min(dp[i-1][0], dp[i-1][1])

    dp.append([red, green, blue])

print(min(dp[n-1]))