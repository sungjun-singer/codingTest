"""

1. 아이디어
- 재귀함수를 돌며 백트래킹을 돈다. 출력해야하는 숫자로 recur함수를 돈다
- 트리 구조로 생각한다.

2. 시간복잡도
- 백트래킹 중복이 없을 경우는 N! 이고 N = 10 까지 가능하다
- 중복이 가능할 경우는 N^N이고 N = 8 까지 가능하다

3. 자료구조
- 결과 값 출력을 위한 배열 res : int[]
- 방문여부 체크를 위한 배열 chk : bool[]

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

res = []
chk = [False] * (n+1)

def recur(num):

    if num == m:
        print(' '. join(map(str, res)))
        return

    for i in range(1, n+1):
        if not chk[i]:
            chk[i] = True
            res.append(i)
            recur(num + 1)
            chk[i] = False
            res.pop()



recur(0)

