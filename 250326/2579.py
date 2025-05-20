"""
1. 아이디어
    - 계단 오르기인데
    - 한번에 1,2계단을 오를수 있고 연속된 세개의 계단을 밟아서는 안된다. 마지막 계단은 무조건 밟아야 한다.
    - 3에 도달할 수 있는 경우는 1 3,/ 2,3
    - 4에 도달할 수 있는 경우는 1,2,4,/ 1,3,4
    - 5에 도달할 수 있는 경우는 2,4,5 / 2,3,5
    - 각 계단별 최대 값을 갱신하면서 배열 순회하면 될듯하다.
    - 이러면 이전계단이 2칸 연속으로 한 값일때는 안된다.
    - 그래서 count랑 값을 같이 넣어서 한다.
2. 시간복잡도
    - 배열 순회 O(n) -> 300
3. 자료구조
    - 계단 점수 배열 -> int []
    - 계단 최대값 배열 -> int []
"""

import sys
input = sys.stdin.readline
n = int(input())

stairs = []

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[0])
    exit(0)

if n == 2:
    print(stairs[0] + stairs[1])
    exit(0)

# 반복문을 3부터 돌리기 위해 1,2계단 값 미리 넣어두기
scores = [ [(stairs[0], 1), (0, 2)], [(stairs[1], 1), (stairs[0]+stairs[1], 2)]  ]

for i in range(2, n):
    new_score = []

    # 두번째 아래 칸에서 값 추가
    new_score.append((max(scores[i-2])[0]+stairs[i], 1))
    # 첫번째 아래 칸에서 값 추가(count가 1인거)
    new_score.append((scores[i-1][0][0] + stairs[i], 2))

    scores.append(new_score)

print(max(scores[n-1])[0])