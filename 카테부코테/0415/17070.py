"""
1. 아이디어
    - 새집으로 이사한 유현이
    - 집 수리를 위해 파이프를 옮기려 하는데
    - 회전 시킬 수 있고, ㅡ ㅣ \ 모양이 가능하다
    - 파이프를 미는 방법은 총 3가지, 오른쪽, 아래, 오른쪽 아래 대각선
    - 가로는 오른쪽 / 대각선
    - 세로는 아래 / 대각선
    - 대각선은 전부

2. 시간복잡도

3. 자료구조

"""

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

def dfs(y, x, status):
    global cnt
    if y == n-1 and x == n-1:
        cnt += 1
        return

    if status == "가로":
        if 0<=x+1<n and not graph[y][x+1]:
            dfs(y, x+1, "가로")
        # if 0<=x+1<n and 0<=y+1<n and not graph[]








