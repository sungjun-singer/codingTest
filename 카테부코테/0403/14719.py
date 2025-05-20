"""
1. 아이디어
    - 빗물이 쌓이는 총량을 구하는 문제
    - 한줄 기준으로 봤을 때 왼쪽과 오른쪽이 모두 막혀있어야 된다.
    - 상태는 "초기", "왼막" 으로 간다.
    - 왼쪽부터 시작해서 막혀있으면 "왼막" 형태 그리고 비어있는 칸 발견할때마다 +1
    - 오른쪽 막혀있으면 "고임" 그리고 전체 카운트에 더하고 0으로 초기화하고 다시 "왼막" 상태
    - 계속 반복하면서 진행
    ====================================================================================
    - 통과 하고 나서 이제 status를 true false로 변경해서 시간 얼마나 주는지 확인
    - false가 초기 true가 왼막 상태
    - 8ms 정도 주네
2. 시간복잡도
    - 이차원 배열을 하나씩 순회 H, W 500 O(N^2) -> 250,000
3. 자료구조
    - 벽 배열 : int [][]
    - 벽 높이 배열 : int []
    - 상태 체크 : str

"""

import sys
input = sys.stdin.readline

h, w = map(int, input().split())

graph = [[1] * w for _ in range(h)]

walls = list(map(int, input().split()))

for i in range(len(walls)):
    for j in range(walls[i]):
        graph[j][i] = 0

res = 0

for i in range(h):
    status = False
    count = 0
    for j in range(w):
        # 0일 때
        if not graph[i][j]:
            if not status:
                status = True
            else:
                res += count
                count = 0
        else:
            if status:
                count += 1

print(res)