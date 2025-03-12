# 2579번
"""
1. 아이디어
    - 계단을 오르는데 연속으로 3칸 오를 수는 없다.
    - 현재 오르는 칸을 오르는 최대값은 이전 두칸의 값을 비교해서 최대값으로 하면 된다.
    - 현재 칸의 최대값을 구하려면 -2 칸의 두 값을 비교하여 큰 값과 -1칸의 count = 1인 거를 올린다.
    - 그러면 (1, -2칸의 최대값), (2, -1칸의 count=1)인 값이 현재 칸에 생긴다.
    - 그러면 맨 마지막 칸에 2개 값이 들어가 있을텐데 두개중에 더 큰거를 출력하면 된다.
2. 시간복잡도
    - 시간복잡도는 O(n)이 된다. 한칸씩 올라가면서 가니깐
3. 자료구조
    - (value, count) 가 들어가는 배열이 필요하다.
    - 입력에서 받은 각 계단의 값을 저장하는 배열이 필요하다
"""

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(int(input()))
    exit(0)

stairs = []
max_value = [[]  for _ in range(n)]


for _ in range(n):
    stairs.append(int(input()))


# 1,2번째 계단 값 넣어주기
max_value[0].append((stairs[0],1))
max_value[1].append((stairs[1], 1))
max_value[1].append((stairs[0] + stairs[1], 2))


for i in range(2, n):
    # -2 칸에서 점수가 높은 값 현재 칸에 count 1로 추가
    under_two_stair = max(max_value[i-2])
    max_value[i].append((under_two_stair[0] + stairs[i], 1))

    # -1칸에서 count 1인 값 현재 칸에 추가 (요소에 count 1부터 넣으니 0번째 값 가져오면 됨)
    max_value[i].append((max_value[i-1][0][0] + stairs[i], 2))

print(max(max_value[n-1])[0])


